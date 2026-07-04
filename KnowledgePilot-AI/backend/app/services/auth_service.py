from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.models.user import User

from app.core.security import (
    hash_password,
    verify_password
)

from app.core.jwt import create_access_token

from app.repositories.user_repository import (
    get_user_by_email,
    create_user
)


# ==========================
# Signup
# ==========================

def signup_user(user_data, db: Session):

    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(
        user_data.password
    )

    user = User(
        name=user_data.name,
        email=user_data.email,
        password=hashed_password
    )

    return create_user(db, user)


# ==========================
# React Login (JSON)
# ==========================

def login_user(login_data, db: Session):

    user = get_user_by_email(
        db,
        login_data.email
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        login_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        {
            "sub": user.email,
            "user_id": user.id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ==========================
# Swagger OAuth Login
# ==========================

def login_user_oauth(
    form_data: OAuth2PasswordRequestForm,
    db: Session
):

    user = get_user_by_email(
        db,
        form_data.username
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        form_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        {
            "sub": user.email,
            "user_id": user.id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }