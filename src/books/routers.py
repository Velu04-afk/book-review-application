

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..config import get_db
from .schemas import BookBase, BookCreate
from .service import get_all_books, create_book

router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.post("/", response_model=BookBase)
async def add_book(
    book: BookCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_book(db, book)


@router.get("/", response_model=list[BookBase])
async def list_books(
    db: AsyncSession = Depends(get_db)
):
    return await get_all_books(db)
