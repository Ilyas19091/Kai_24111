import os
import shutil
import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [logging.FileHandler('file_organizer.log', encoding='utf-8'),
                logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Расширения файлов
IMAGES = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff']
AUDIOS = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a']
VIDEOS = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v']
ARCHIVES = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz']
DOCUMENTS = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.rtf']

# Название папок для организации файлов
images_folder = os.path.join(downloads_path, "Images")
audios_folder = os.path.join(downloads_path, "Audios")
videos_folder = os.path.join(downloads_path, "Videos")
archives_folder = os.path.join(downloads_path, "Archives")
documents_folder = os.path.join(downloads_path, "Documents")

def unique_file(filepath):
    if not os.path.exists(filepath):
        return filepath
    base, ext = os.path.splitext(filepath)
    counter = 1
    while True:
        new_filepath = f"{base} ({counter}){ext}"
        if not os.path.exists(new_filepath):
            return new_filepath
        counter += 1

logger.info(f"Начало сортировки файлов в: {downloads_path}")

for file in os.listdir(downloads_path):
    filepath = os.path.join(downloads_path, file)
    if not os.path.isfile(filepath):
        continue

    moved = False

    if file.endswith(tuple(IMAGES)):
        os.makedirs(images_folder, exist_ok=True)
        dstpath = os.path.join(images_folder, file)
        dstpath = unique_file(dstpath)
        shutil.move(filepath, dstpath)
        logger.info(f"Перемещен: {file} -> Images/")
        moved = True
    elif file.endswith(tuple(AUDIOS)):
        os.makedirs(audios_folder, exist_ok=True)
        dstpath = os.path.join(audios_folder, file)
        dstpath = unique_file(dstpath)
        shutil.move(filepath, dstpath)
        logger.info(f"Перемещен: {file} -> Audios/")
        moved = True
    elif file.endswith(tuple(VIDEOS)):
        os.makedirs(videos_folder, exist_ok=True)
        dstpath = os.path.join(videos_folder, file)
        dstpath = unique_file(dstpath)
        shutil.move(filepath, dstpath)
        logger.info(f"Перемещен: {file} -> Videos/")
        moved = True
    elif file.endswith(tuple(ARCHIVES)):
        os.makedirs(archives_folder, exist_ok=True)
        dstpath = os.path.join(archives_folder, file)
        dstpath = unique_file(dstpath)
        shutil.move(filepath, dstpath)
        logger.info(f"Перемещен: {file} -> Archives/")
        moved = True
    elif file.endswith(tuple(DOCUMENTS)):
        os.makedirs(documents_folder, exist_ok=True)
        dstpath = os.path.join(documents_folder, file)
        dstpath = unique_file(dstpath)
        shutil.move(filepath, dstpath)
        logger.info(f"Перемещен: {file} -> Documents/")
        moved = True

    if not moved:
        logger.info(f"Пропущен: {file} (неизвестный тип)")
    
logger.info("Сортировка файлов завершена")
