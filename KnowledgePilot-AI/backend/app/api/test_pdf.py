from fastapi import APIRouter

from app.utils.pdf import extract_text_from_pdf

router = APIRouter(
    tags=["Testing"]
)


@router.get("/test-pdf")

def test_pdf():

    text = extract_text_from_pdf(
        "uploads/1/MachineLearning.pdf"
    )

    return {

        "text": text[:1000]

    }