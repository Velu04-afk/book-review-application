from pydantic import BaseModel
from datetime import datetime


class ReviewCreate(BaseModel):
    reviewer_name: str
    review: str


class ReviewOut(BaseModel):
    book_id: int
    reviewer_name: str
    review: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
