from datetime import datetime
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str


# For PostDisplay
class User(BaseModel):
    username: str
    id: int

    class Config:
        orm_mode = True


# For PostDisplay
class Comment(BaseModel):
    message: str
    username: str
    timestamp: datetime

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    username: str
    message: str
    post_id: int
