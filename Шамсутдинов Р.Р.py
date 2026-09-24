import os, shutil, time
from pathlib import Path

TARGET = Path(r"C:\Users\User\Downloads")
EXTS = {
    "Документы": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".csv", ".rtf"],
    "Изображения": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".psd", ".ai"],
    "Видео": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Музыка и Аудио": [".mp3", ".wav", ".flac", ".ogg", ".m4a", ".aac"],
    "Архивы": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Программы и Инсталляторы": [".exe", ".msi", ".dmg", ".iso", ".sh"],
    "Книги": [".epub", ".fb2", ".djvu", ".mobi"]
}


def scan_and_move():
    for f in list(TARGET.rglob("*")):
        if f.is_file() and not any(p in EXTS or p == "Разное" for p in f.relative_to(TARGET).parts[:-1]):
            dest_dir = TARGET / next((k for k, v in EXTS.items() if f.suffix.lower() in v), "Разное")
            dest_dir.mkdir(exist_ok=True)

            dest, c = dest_dir / f.name, 1
            while dest.exists():
                dest = dest_dir / f"{f.stem}_{c}{f.suffix}"
                c += 1
            try:
                shutil.move(str(f), str(dest))
            except:
                pass

    for r, dirs, _ in os.walk(str(TARGET), topdown=False):
        for d in dirs:
            if d not in EXTS and d != "Разное":
                try:
                    os.rmdir(os.path.join(r, d))
                except:
                    pass


if __name__ == "__main__":
    print("Разгребаем старые завалы и включаем постоянный мониторинг...")
    while True:
        scan_and_move()
        time.sleep(5)  # Проверяет папку каждые 5 секунд