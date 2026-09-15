import os, shutil, time
from pathlib import Path

p = Path.home() / 'Downloads'

c = {
    'Изображения': ['.jpg','.jpeg','.png','.gif','.bmp','.svg','.webp'],
    'Документы': ['.pdf','.docx','.doc','.txt','.xlsx','.pptx'],
    'Архивы': ['.zip','.rar','.7z','.tar','.gz'],
    'Музыка': ['.mp3','.wav','.flac','.aac','.ogg'],
    'Видео': ['.mp4','.avi','.mkv','.mov','.wmv'],
    'Программы': ['.exe','.msi','.dmg','.pkg','.deb'],
    'Код': ['.py','.js','.html','.css','.cpp','.java']
}

for i in c: (p/i).mkdir(exist_ok=True)

def cat(f):
    for k,v in c.items():
        if f.suffix.lower() in v: return k
    return 'Другое'

def unique(folder, name):
    if not (folder/name).exists(): return name
    s,e = Path(name).stem, Path(name).suffix
    i = 1
    while (folder/f"{s}_{i}{e}").exists(): i += 1
    return f"{s}_{i}{e}"

def move(f, seen):
    if not f.is_file() or f.name.startswith('.'): return
    fp = str(f.absolute())
    if fp in seen: return
    folder = p/cat(f)
    name = unique(folder, f.name)
    shutil.move(str(f), str(folder/name))
    seen.add(fp)
    seen.add(str((folder/name).absolute()))
    print(f"✅ {f.name} → {cat(f)}/{name}")

print(f"\n📂 {p}\n")
seen = set()

for f in p.iterdir(): move(f, seen)
for r,_,fs in os.walk(p):
    for f in fs: seen.add(str(Path(r)/f))

print(f"📊 {len(seen)} файлов\n🔄 Мониторинг...\n")
total = 0

while 1:
    try:
        for f in p.iterdir():
            if f.is_file() and not f.name.startswith('.'):
                fp = str(f.absolute())
                if fp not in seen:
                    move(f, seen)
                    seen.add(fp)
                    total += 1
        time.sleep(30)
    except KeyboardInterrupt:
        print(f"\n⏹️  Перемещено: {total} файлов")
        break