import os
import shutil
from pathlib import Path
import zipfile

# Step 0: Clean current directory: remove all directories and subdirs in '.'
for item in Path('.').iterdir():
    if item.is_dir():
        shutil.rmtree(item)
print("All directories in the current directory have been deleted.")

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
    for html in subdir.glob('*.html'):
        # Rename - remove the last 5 characters (".html")
        new_name = html.with_name(html.name[:-5])
        html.rename(new_name)
        
        # Create new directory for unzipping
        extract_dir = new_name.parent / new_name.name[:-4]  # Same name as the zip file, now a folder
        extract_dir.mkdir(exist_ok=True)

        # Try to unzip the file as a zip archive into new directory
        try:
            # Unzip into a new dir
            with zipfile.ZipFile(new_name, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            print(f"Unzipped: {new_name} -> {extract_dir}")

            # Delete the zip file after extraction
            new_name.unlink()
            print(f"Deleted: {new_name}")

        except zipfile.BadZipFile:
            # Clean up by deleting the empty/newly-created directory
            shutil.rmtree(extract_dir)
            print(f"Skipped (not a zip): {new_name}")