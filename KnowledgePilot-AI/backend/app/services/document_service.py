import os
import os

from app.repositories.document_repository import delete_document

from app.services.vector_service import delete_document_vectors
from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from app.models.document import Document

from app.repositories.document_repository import (
    create_document
)
from app.repositories.document_repository import (
    create_document,
    get_documents_by_user
)
from app.utils.pdf import (
    extract_text_from_pdf
)

from app.utils.chunker import (
    chunk_text
)

from app.services.vector_service import (
    store_chunks
)

UPLOAD_FOLDER = "uploads"


def upload_document(
    file: UploadFile,
    current_user,
    db: Session
):

    # ==============================
    # 1. Check PDF
    # ==============================

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # ==============================
    # 2. Create User Folder
    # ==============================

    user_folder = os.path.join(
        UPLOAD_FOLDER,
        str(current_user.id)
    )

    os.makedirs(
        user_folder,
        exist_ok=True
    )

    # ==============================
    # 3. File Path
    # ==============================

    file_path = os.path.join(
        user_folder,
        file.filename
    )

    # ==============================
    # 4. Save PDF
    # ==============================

    with open(file_path, "wb") as buffer:

        content = file.file.read()

        buffer.write(content)

    # ==============================
    # 5. Save Metadata
    # ==============================

    document = Document(
        filename=file.filename,
        filepath=file_path,
        file_size=len(content),
        uploaded_by=current_user.id
    )

    document = create_document(
        db,
        document
    )

    # ==============================
    # 6. Extract Text
    # ==============================

    text = extract_text_from_pdf(
        file_path
    )

    # ==============================
    # 7. Chunk Text
    # ==============================

    chunks = chunk_text(
        text
    )

    # ==============================
    # 8. Store Embeddings
    # ==============================

    store_chunks(
        document.id,
        chunks
    )

    # ==============================
    # 9. Return Document
    # ==============================

    return document
def list_documents(
    current_user,
    db: Session
):

    return get_documents_by_user(
        db,
        current_user.id
    )
def remove_document(
    document_id,
    db
):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if document is None:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    # Delete PDF file

    if os.path.exists(document.filepath):

        os.remove(document.filepath)

    # Delete vectors

    delete_document_vectors(document.id)

    # Delete DB row

    delete_document(
        db,
        document.id
    )

    return {

        "message": "Document deleted successfully"

    }