from app.services.file_scanner import scan_folder

files = scan_folder(r"D:\test-folder")

for file in files:
    print(file)