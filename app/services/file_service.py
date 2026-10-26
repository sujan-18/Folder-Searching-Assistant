from sqlalchemy.orm import Session

from app.repositories.repositories import get_all_files, create_file
from app.repositories.repositories import get_file_by_id, delete_file, search_files,get_file_by_path

from app.services.file_scanner import scan_folder


def get_files(db: Session):
    return get_all_files(db)


def add_file(db: Session, file_data: dict):
    return create_file(db, file_data)

def get_file(db: Session, file_id: int):
    return get_file_by_id(db, file_id)

def remove_file(db: Session, file_id: int):
    return delete_file(db, file_id)

def find_files(db: Session, query: str):
    return search_files(db, query)


def index_folder(db: Session, folder_path: str):
    scanned_files = scan_folder(folder_path)

    indexed_count = 0
    updated_count = 0
    skipped_count = 0

    for file_data in scanned_files:
        existing_file = get_file_by_path(db, file_data["path"])

        # 1. New file: add it to the database
        if existing_file is None:
            create_file(db, file_data)
            indexed_count += 1
            continue

        # 2. Existing file: check whether it has changed
        if (
            existing_file.size != file_data["size"]
            or existing_file.modified_at != file_data["modified_at"]
        ):
            existing_file.name = file_data["name"]
            existing_file.extension = file_data["extension"]
            existing_file.size = file_data["size"]
            existing_file.modified_at = file_data["modified_at"]

            db.commit()
            db.refresh(existing_file)
            updated_count += 1
        else:
            # 3. No changes: keep the existing record
            skipped_count += 1

    return {
        "indexed": indexed_count,
        "updated": updated_count,
        "skipped": skipped_count
    }
