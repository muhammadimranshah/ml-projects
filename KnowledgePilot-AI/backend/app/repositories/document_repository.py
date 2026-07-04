from sqlalchemy.orm import Session

from app.models.document import Document
from sqlalchemy.orm import Session
from app.models.document import Document


def delete_document(db: Session, document_id: int):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if document:

        db.delete(document)

        db.commit()

    return document

def create_document(db: Session, document: Document):

    db.add(document)
    db.commit()
    db.refresh(document)

    return document


def get_documents_by_user(
    db: Session,
    user_id: int
):

    return (
        db.query(Document)
        .filter(Document.uploaded_by == user_id)
        .order_by(Document.id.desc())
        .all()
    )