from pathlib import Path
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
DOWNLOADS = Path.home() / "Downloads"
CATEGORIES = {
    "Изображения": ".jpg .jpeg .png .gif .webp .bmp .svg .ico".split(),
    "Видео": ".mp4 .mkv .avi .mov .wmv .flv .webm".split(),
    "Музыка": ".mp3 .wav .flac .aac .ogg .m4a .opus".split(),
    "Документы": ".pdf .doc .docx .txt .rtf .odt .xls .xlsx .csv .ppt .pptx".split(),
    "Архивы": ".zip .rar .7z .tar .gz .bz2 .xz .iso".split(),
    "Программы": ".exe .msi .msix .bat .cmd .apk".split(),
    "Код": ".py .js .ts .html .css .json .xml .yaml .yml .cpp .c .h .java .php .sql".split(),
    "Торренты": [".torrent"]
}
IGNORE = {".crdownload", ".part", ".tmp", ".download"}
def category(file):
    ext = file.suffix.lower()
    for folder, extensions in CATEGORIES.items():
        if ext in extensions:
            return folder
    return "Другое"
def move(file):
    if not file.is_file() or file.suffix.lower() in IGNORE:
        return
    time.sleep(2)
    try:
        size = file.stat().st_size
        time.sleep(1)
        if file.stat().st_size != size:
            return
        folder = DOWNLOADS / category(file)
        folder.mkdir(exist_ok=True)
        destination = folder / file.name
        n = 1
        while destination.exists():
            destination = folder / f"{file.stem} ({n}){file.suffix}"
            n += 1
        shutil.move(file, destination)
    except (FileNotFoundError, PermissionError):
        pass
class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            move(Path(event.src_path))
for file in DOWNLOADS.iterdir():
    move(file)
observer = Observer()
observer.schedule(Handler(), str(DOWNLOADS), recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()