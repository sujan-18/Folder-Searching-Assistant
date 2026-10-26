from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.services.file_service import add_file, find_files, get_file, get_files, index_folder, remove_file
from app.schemas.file import FileCreate, FileResponse
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/files", response_model=list[FileResponse])
def get_files_endpoint(db: Session = Depends(get_db)):
    return get_files(db)


@router.get("/files/{file_id}", response_model=FileResponse)
def get_file_endpoint(
    file_id: int,
    db: Session = Depends(get_db)
):
    file = get_file(db, file_id)

    if file is None:
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return file


@router.post("/files", response_model=FileResponse, status_code=201)
def create_file_endpoint(
    file_data: FileCreate, 
    db: Session = Depends(get_db)
):
    return add_file(db, file_data.model_dump())

@router.delete("/files/{file_id}")
def delete_file_endpoint(
    file_id: int,
    db: Session = Depends(get_db)
):
    deleted = remove_file(db, file_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return {"message": "File metadata deleted successfully"}

@router.get("/search", response_model=list[FileResponse])
def search_files_endpoint(
    q: str = Query(min_length=1, max_length=100),
    db: Session = Depends(get_db)
):
    q = q.strip()

    if not q:
        raise HTTPException(
            status_code=422,
            detail="Search query cannot be empty"
        )

    return find_files(db, q)

@router.post("/index")
def index_folder_endpoint(
    folder_path: str,
    db: Session = Depends(get_db)
):
    return index_folder(db, folder_path)