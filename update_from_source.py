import os
import shutil
from pathlib import Path
import zipfile

# Step 0: Clean current directory: remove all directories and subdirs in '.'
for item in Path('.').iterdir():
    if item.name == '.git' or item.name.endswith('.py'):
        continue
    # Remove files and directories
    if item.is_dir():
        shutil.rmtree(item)
    else:
        item.unlink()

print("All items in the current directory have been deleted.")

# Step 1: Copy everything from ../cyberverse_concepts to current dir
src = Path("../cyberverse_concepts")
dst = Path("./")

def copytree(src, dst):
    for item in src.iterdir():
        s = src / item.name
        d = dst / item.name
        if s.is_dir():
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

copytree(src, dst)

# Step 2: Process each immediate subdirectory of root
for subdir in [p for p in dst.iterdir() if p.is_dir()]:
    for file in (f for pattern in ('*.html', '*.zip') for f in subdir.glob(pattern)):
        # Rename - change html to zip
        if file.name.endswith(".html"):
            new_name = file.with_name(file.name[:-5])
            file.rename(new_name)
            file = new_name
        
        # Create new directory for unzipping
        extract_dir =  file.parent /  file.name[:-4]  # Same name as the zip file, now a folder
        extract_dir.mkdir(exist_ok=True)

        # Try to unzip the file as a zip archive into new directory
        try:
            # Unzip into a new dir
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            # Delete the zip file after extraction
            file.unlink()
            print(f"Unzipped: {file.name} -> {extract_dir}")

        except zipfile.BadZipFile:
            # Clean up by deleting the empty/newly-created directory
            shutil.rmtree(extract_dir)
            print(f"Skipped (not a zip): {file.name}")