from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from auth import authentication
from db import models
from db.database import engine
from routers import comments, posts, users

app = FastAPI()
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(authentication.router)


@app.get("/")
def root():
    return "Hello"


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="images"), name="images")
