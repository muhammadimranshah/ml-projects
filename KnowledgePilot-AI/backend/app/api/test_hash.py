from fastapi import APIRouter

from app.core.security import hash_password

router = APIRouter()

@router.get("/test-hash")
def test_hash():

    password = "Imran123"

    hashed = hash_password(password)

    return {
        "original": password,
        "hashed": hashed
    }