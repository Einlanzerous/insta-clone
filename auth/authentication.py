from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from auth.oauth2 import create_access_token
from db.database import get_db
from db.hashing import Hash
from db.models import DBUser

router = APIRouter(tags=["Auth"])


@router.post("/login")
def login(
    db: Session = Depends(get_db), request: OAuth2PasswordRequestForm = Depends()
):
    user = db.query(DBUser).filter(DBUser.username == request.username).first()

    if not user and not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials"
        )

    access_token = create_access_token(data={"username": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.username,
    }
