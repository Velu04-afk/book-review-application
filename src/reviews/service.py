from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Review
from .schemas import ReviewCreate


async def add_review_for_book(db: AsyncSession, book_id: int, review_data: ReviewCreate):
    new_review = Review(
        book_id=book_id,
        reviewer_name=review_data.reviewer_name,
        review=review_data.review
    )
    db.add(new_review)
    await db.commit()
    await db.refresh(new_review)
    return new_review


async def get_reviews_for_book(db: AsyncSession, book_id: int):
    result = await db.execute(select(Review).where(Review.book_id == book_id))
    return result.scalars().all()
