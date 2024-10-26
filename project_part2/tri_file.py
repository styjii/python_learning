from pathlib import Path

dirs = {
    ".png": "Images",
    ".jpeg": "Images",
    ".jpg": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mp3": "Musiques",
    ".wav": "Musiques",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".exe": "Programmes"
}

tri_dir = Path.home() / "Downloads"
files = [f for f in tri_dir.iterdir() if f.is_file()]

for f in files :
    # create folder
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    # mouve the file in the folder
    f.rename(output_dir / f.name)