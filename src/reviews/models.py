from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from ..config import Base


class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey(
        "books.book_id", ondelete="CASCADE"), nullable=False)
    reviewer_name = Column(String(255), nullable=False)
    review = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(
    ), onupdate=func.now(), nullable=False)
