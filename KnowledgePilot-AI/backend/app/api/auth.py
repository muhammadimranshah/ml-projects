from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
    Token
)

from app.services.auth_service import (
    signup_user,
    login_user,
    login_user_oauth
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ==========================
# Signup
# ==========================

@router.post(
    "/signup",
    response_model=UserResponse
)
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return signup_user(user, db)


# ==========================
# React / Frontend Login
# JSON:
# {
#   "email":"abc@gmail.com",
#   "password":"123"
# }
# ==========================

@router.post(
    "/login",
    response_model=Token
)
def login(
    login: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(login, db)


# ==========================
# Swagger Authorize Login
# x-www-form-urlencoded
# ==========================

@router.post(
    "/token",
    response_model=Token
)
def token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user_oauth(form_data, db)