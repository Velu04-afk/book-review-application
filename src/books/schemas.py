from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BookBase(BaseModel):
    book_id: int
    name: str
    price: int
    genre: Optional[str] = None
    author: Optional[str] = None
    publication: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enables ORM model compatibility


class BookCreate(BaseModel):
    name: str
    price: int
    genre: Optional[str] = None
    author: Optional[str] = None
    publication: Optional[str] = None
