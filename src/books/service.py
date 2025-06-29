from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Book
from .schemas import BookCreate


async def get_all_books(db: AsyncSession):
    # Fetch all books
    result = await db.execute(select(Book))
    books = result.scalars().all()
    return books


async def create_book(db: AsyncSession, book: BookCreate):
    # Add a new book
    new_book = Book(**book.dict())
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    return new_book
