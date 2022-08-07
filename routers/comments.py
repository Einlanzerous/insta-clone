from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from auth.oauth2 import get_current_user
from db import db_comments
from db.database import get_db
from routers.schemas import CommentBase, UserAuth

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.get("/{post_id}")
def get_by_post_id(post_id: int, db: Session = Depends(get_db)):
    return db_comments.get_all_for_post_id(db, post_id)


@router.post("")
def create(
    request: CommentBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    return db_comments.create(db, request)
