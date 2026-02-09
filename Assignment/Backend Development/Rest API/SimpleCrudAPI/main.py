from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Database Setup
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/test_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# SQLAlchemy Model
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)

# Pydantic Schema
class UserCreate(BaseModel):
    email: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserDB(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
