from pathlib import Path
from datetime import datetime, timezone


def scan_folder(folder_path: str):
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError("Folder does not exist")

    if not folder.is_dir():
        raise NotADirectoryError("Path is not a folder")

    files = []

    for item in folder.iterdir():
        if item.is_file():
            files.append({
                "name": item.name,
                "path": str(item.resolve()),
                "extension": item.suffix.lower(),
                "size": item.stat().st_size,
                "modified_at": datetime.fromtimestamp(
                    item.stat().st_mtime,
                    tz=timezone.utc
                ),
                
            })

    return files