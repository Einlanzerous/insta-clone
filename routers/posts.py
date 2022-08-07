import shutil
from pathlib import Path
from typing import List
from uuid import uuid4

from fastapi import APIRouter, Depends, File, UploadFile, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from auth.oauth2 import get_current_user
from db import db_posts
from db.database import get_db
from routers.schemas import PostBase, PostDisplay, UserAuth

router = APIRouter(
    prefix="/post",
    tags=["Posts"],
)

image_url_types = ["absolute", "relative"]


@router.post("", response_model=PostDisplay)
def create(
    request: PostBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid Params- image_url_type must be one of {image_url_types}.",
        )

    return db_posts.create(db, request)


@router.get("/all", response_model=List[PostDisplay])
def get_all(db: Session = Depends(get_db)):
    return db_posts.get_all(db)


@router.post("/image")
def upload_image(
    image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)
):
    file_ext = Path(image.filename).suffix
    new_file_name = f"{uuid4()}{file_ext}"
    relative_path = f"images/{new_file_name}"

    with open(relative_path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": new_file_name}


@router.delete("/delete/{id}")
def delete_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    return db_posts.delete(db, id, current_user.id)
