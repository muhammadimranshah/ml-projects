from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File
)
from app.services.document_service import (
    upload_document,
    remove_document
)
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.core.dependencies import get_current_user

from app.schemas.document import DocumentResponse

from app.services.document_service import (
    upload_document,
    list_documents
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post(
    "/upload",
    response_model=DocumentResponse
)
def upload_pdf(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return upload_document(
        file,
        current_user,
        db
    )


@router.get(
    "/",
    response_model=list[DocumentResponse]
)
def get_documents(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return list_documents(
        current_user,
        db
    )
@router.delete("/{document_id}")
def delete_document_api(

    document_id: int,

    current_user=Depends(get_current_user),

    db: Session = Depends(get_db)

):

    return remove_document(
        document_id,
        db
    )