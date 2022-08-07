from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.hashing import Hash
from db.models import DBUser
from routers.schemas import UserBase


def create(db: Session, request: UserBase):
    user = DBUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_by_username(db: Session, username: str):
    user = db.query(DBUser).filter(DBUser.username == username).first()

    if not user:
        raise HTTPException(
            status=status.HTTP_404_NOT_FOUND,
            detail=f"User not found with username: {username}",
        )

    return user
