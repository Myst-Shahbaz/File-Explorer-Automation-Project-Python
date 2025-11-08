import os
import shutil

# Set the folder to organize
path = r"B:\Python Auto"

# Define file type categories and corresponding folder names

file_types = {
    "Images": (".png", ".jpg", ".jpeg", ".gif"),
    "Excel Files": (".xls", ".xlsx", ".csv"),
    "Text Files": (".txt",),
    "PDF Files": (".pdf",),
    "Documents": (".doc", ".docx"),
    "Videos": (".mp4", ".mov", ".avi"),
    # You can add more categories here
}

# initialize and list all files before organizing

all_files = os.listdir(path)
print("Files before organizing:")
print(*all_files, sep="\n")
print("\nOrganizing...\n")

# Create folders if they don't exist
for folder in file_types:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# Move files to corresponding folders
for file in all_files:
    file_path = os.path.join(path, file)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue
    
    # Check file extension and move
    for folder, extensions in file_types.items():
        if file.lower().endswith(extensions):
            shutil.move(file_path, os.path.join(path, folder, file))
            break  # Stop checking once moved

# Print files after organizing
print("Files after organizing:")
for folder in all_files:
    print(folder)
    folder_path = os.path.join(path, folder)
    if os.path.isdir(folder_path):  
        for organized_file in os.listdir(folder_path):
            print(f"  - {organized_file}")