from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import DBPost
from routers.schemas import PostBase


def create(db: Session, request: PostBase):
    post = DBPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=request.creator_id,
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


def get_all(db: Session):
    return db.query(DBPost).all()


def delete(db: Session, id: int, user_id: int):
    post = db.query(DBPost).filter(DBPost.id == id).first()

    if not post:
        raise HTTPException(
            status=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found",
        )

    if post.user_id != user_id:
        raise HTTPException(
            status=status.HTTP_403_FORBIDDEN,
            detail=f"User with id {user_id} is not the creator of post {id}",
        )

    db.delete(post)
    db.commit()

    return "ok"
