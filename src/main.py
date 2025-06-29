# src/main.py

from fastapi import FastAPI
from .books.routers import router as books_router
from .reviews.routers import router as review_router

app = FastAPI()

app.include_router(books_router)
app.include_router(review_router)


@app.get("/")
async def root():
    return {"message": "Book Review Application API is running!"}
