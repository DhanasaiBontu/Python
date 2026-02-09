from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("UserDB", back_populates="items")


# Add relationship to UserDB
from .models import UserDB
UserDB.items = relationship("ItemDB", back_populates="owner")
