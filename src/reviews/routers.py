from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import get_db
from . import schemas, service

router = APIRouter()


@router.post("/books/{book_id}/reviews", response_model=schemas.ReviewCreate, status_code=201)
async def add_review_for_book(
    book_id: int,
    review_data: schemas.ReviewCreate,
    db: AsyncSession = Depends(get_db)
):
    review = await service.add_review_for_book(db, book_id, review_data)
    return review


@router.get("/books/{book_id}/reviews", response_model=list[schemas.ReviewOut])
async def get_reviews_for_book(
    book_id: int,
    db: AsyncSession = Depends(get_db)
):
    reviews = await service.get_reviews_for_book(db, book_id)
    if not reviews:
        raise HTTPException(
            status_code=404, detail="No reviews found for this book.")
    return reviews
