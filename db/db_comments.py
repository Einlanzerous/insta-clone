from datetime import datetime

from sqlalchemy.orm.session import Session

from db.models import DBComment
from routers.schemas import CommentBase


def create(db: Session, request: CommentBase):
    comment = DBComment(
        message=request.message,
        username=request.username,
        post_id=request.post_id,
        timestamp=datetime.now(),
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)


def get_all_for_post_id(db: Session, post_id: int):
    return db.query(DBComment).filter(DBComment.post_id == post_id).all()
