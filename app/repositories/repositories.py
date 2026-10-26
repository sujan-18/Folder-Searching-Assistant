from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.file import File


def get_all_files(db: Session):
    statement = select(File)
    result = db.execute(statement)

    return result.scalars().all()

def get_file_by_id(db: Session, file_id: int):
    statement = select(File).where(File.id == file_id)

    result = db.execute(statement)

    return result.scalar_one_or_none()

def create_file(db: Session, file_data: dict):
    new_file = File(**file_data)

    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return new_file

def delete_file(db: Session, file_id: int):
    file = db.get(File, file_id)

    if file is None:
        return False

    db.delete(file)
    db.commit()

    return True

def search_files(db: Session, query: str):
    statement = select(File).where(
        File.name.ilike(f"%{query}%")
    )

    result = db.execute(statement)

    return result.scalars().all()

def get_file_by_path(db: Session, path: str):
    statement = select(File).where(File.path == path)
    result = db.execute(statement)
    return result.scalar_one_or_none()