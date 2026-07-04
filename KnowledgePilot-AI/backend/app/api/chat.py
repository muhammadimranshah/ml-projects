from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest,
    ChatResponse
)

from app.services.chat_service import (
    ask_question
)

router = APIRouter(

    prefix="/chat",

    tags=["Chat"]

)

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    
    answer = ask_question(request.question)

    return {
        "answer": answer   # ✅ string only
    }