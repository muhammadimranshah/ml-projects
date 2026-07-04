from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.database import get_db
from app.repositories.user_repository import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)
def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db)

):

    try:

        payload = jwt.decode(

            token,

            settings.SECRET_KEY,

            algorithms=[settings.ALGORITHM]

        )

    except JWTError:

        raise HTTPException(

            status_code=401,

            detail="Invalid Token"

        )

    email = payload.get("sub")

    user = get_user_by_email(

        db,

        email
    )

    if user is None:

        raise HTTPException(

            status_code=401,

            detail="User not found"

        )

    return user