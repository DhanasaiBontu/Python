from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Session
from pydantic import BaseModel
from typing import List

DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

app = FastAPI()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="comments")

Base.metadata.create_all(bind=engine)

class CommentCreateSchema(BaseModel):
    content: str

class CommentResponseSchema(CommentCreateSchema):
    id: int
    class Config:
        orm_mode = True

class PostCreateSchema(BaseModel):
    title: str
    content: str

class PostResponseSchema(PostCreateSchema):
    id: int
    comments: List[CommentResponseSchema] = []
    class Config:
        orm_mode = True

class UserCreateSchema(BaseModel):
    username: str

class UserResponseSchema(UserCreateSchema):
    id: int
    posts: List[PostResponseSchema] = []
    class Config:
        orm_mode = True

def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.post("/users", response_model=UserResponseSchema)
def create_user(user_data: UserCreateSchema, db: Session = Depends(get_db_session)):
    user = User(username=user_data.username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/users/{user_id}/posts", response_model=PostResponseSchema)
def create_post_for_user(user_id: int, post_data: PostCreateSchema, db: Session = Depends(get_db_session)):
    post = Post(title=post_data.title, content=post_data.content, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.post("/posts/{post_id}/comments", response_model=CommentResponseSchema)
def add_comment_to_post(post_id: int, comment_data: CommentCreateSchema, db: Session = Depends(get_db_session)):
    comment = Comment(content=comment_data.content, post_id=post_id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment