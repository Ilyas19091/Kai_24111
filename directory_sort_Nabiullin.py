# Набиуллин Азамат 24111 2026

import argparse
import os
from pathlib import Path
import shutil

def move_file(src, dest):
    filename = Path(src).name
    if Path(dest, filename).exists():
        print(f"Log: Failed to move. File '{filename}' already exists at '{dest}'")
    else:
        shutil.move(src, dest)
        print(f"Log: Moved '{filename}' to '{dest}'")

document_extensions = [".pdf", ".doc", ".docx", ".txt"]
image_extensions = [".png", ".jpeg", ".jpg", ".webp", ".gif", ".avif", ".bmp", ".svg", ".tiff"]
archive_extensions = [".zip", ".7z", ".tar", ".gz", ".rar"]
video_extensions = [".mp4", ".avi", ".mkv", ".webm", ".wmv", ".mov"]
audio_extensions = [".wav", ".aiff", ".flac", ".alac", ".ape", ".mp3", ".aac", ".m4a", ".ogg", ".wma"]
app_extensions = [".exe"]

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="Абсолютный путь к папке 'Загрузки'")
args = parser.parse_args()

directory = Path(args.path)

os.makedirs(Path(directory, "Документы"), exist_ok=True)
os.makedirs(Path(directory, "Картинки"), exist_ok=True)
os.makedirs(Path(directory, "Архивы"), exist_ok=True)
os.makedirs(Path(directory, "Видео"), exist_ok=True)
os.makedirs(Path(directory, "Аудио"), exist_ok=True)
os.makedirs(Path(directory, "Приложения"), exist_ok=True)
os.makedirs(Path(directory, "Другое"), exist_ok=True)

files = [f for f in directory.iterdir() if f.is_file()] 
for file in files:
    filepath = Path(directory, file)
    if filepath.suffix in document_extensions:
        move_file(filepath, Path(directory, "Документы"))
    elif filepath.suffix in image_extensions:
        move_file(filepath, Path(directory, "Картинки"))
    elif filepath.suffix in archive_extensions:
        move_file(filepath, Path(directory, "Архивы"))
    elif filepath.suffix in video_extensions:
        move_file(filepath, Path(directory, "Видео"))
    elif filepath.suffix in audio_extensions:
        move_file(filepath, Path(directory, "Аудио"))
    elif filepath.suffix in app_extensions:
        move_file(filepath, Path(directory, "Приложения"))
    else:
        move_file(filepath, Path(directory, "Другое"))
