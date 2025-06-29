from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship
from ..config import Base


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    genre = Column(String(255), nullable=True)
    author = Column(String(255), nullable=True)
    publication = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(
    ), onupdate=func.now(), nullable=False)
