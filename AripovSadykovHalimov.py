# Тимур Арипов
# Искандер Садыков
# Ирик Халимов


import os
from pathlib import Path
from datetime import datetime

downloads = Path.home() / "Downloads"

extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Programs": [".exe", ".msi", ".deb", ".rpm", ".dmg", ".appimage"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".ps1", ".php", ".html", ".css"],
    "Torrents": [".torrent"]
}

log_folder = downloads / "logs"
if not log_folder.exists():
    log_folder.mkdir()

log_lines = []
log_lines.append(f"=== {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")

for folder in extensions:
    path = downloads / folder
    if not path.exists():
        path.mkdir()
        print(f"создал папку {folder}")
        log_lines.append(f"создал папку {folder}")

if not (downloads / "Other").exists():
    (downloads / "Other").mkdir()
    print("создал папку Other")
    log_lines.append("создал папку Other")

moved = 0
skipped = 0

for file in downloads.iterdir():
    if file.is_dir():
        continue

    ext = file.suffix.lower()

    destination = "Other"
    for folder, exts in extensions.items():
        if ext in exts:
            destination = folder
            break

    new_path = downloads / destination / file.name

    counter = 1
    while new_path.exists():
        stem = file.stem
        suffix = file.suffix
        new_name = f"{stem} ({counter}){suffix}"
        new_path = downloads / destination / new_name
        counter += 1

    try:
        os.rename(file, new_path)
        print(f"{file.name} -> {destination}/{new_path.name}")
        log_lines.append(f"{file.name} -> {destination}/{new_path.name}")
        moved += 1
    except Exception as e:
        print(f"ошибка с {file.name}: {e}")
        log_lines.append(f"ошибка с {file.name}: {e}")
        skipped += 1

print(f"\nвсего перемещено: {moved}")
print(f"пропущено: {skipped}")
log_lines.append(f"всего перемещено: {moved}")
log_lines.append(f"пропущено: {skipped}")
log_lines.append("")

log_file = log_folder / f"organize_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(log_file, "w", encoding="utf-8") as f:
    f.write("\n".join(log_lines))
