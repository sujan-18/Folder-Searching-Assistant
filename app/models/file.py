from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from datetime import datetime




class File(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    path: Mapped[str] = mapped_column(String(1000))
    extension: Mapped[str] = mapped_column(String(20))
    size: Mapped[int]
    modified_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
        nullable=False
)

