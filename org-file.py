import os, shutil

def logError(fileName, path):
    print(f"File with name {fileName} already exists in {path}") 

def logMoving(fileName, path):
    print(f"The file {fileName} has moved in {path}") 
home_dir = os.path.expanduser("~")
downloadPath = os.path.join(home_dir, "Downloads")
imagesPath = os.path.join(downloadPath, "Images")
docPath = os.path.join(downloadPath, "Documents")
archivePath = os.path.join(downloadPath, "Archives")
applicationPath = os.path.join(downloadPath, "Aplications")

files = os.listdir(downloadPath)

imageFormats = [".png", ".jpg", ".svg"]
docFormats = [".doc",".docx",".txt", ".pdf", ".xlsx", ".xls"]
archiveFormats =[".zip", ".rar", ".7z"]
applicationFormats = [".exe", ".msi", ".dll"]

for i in range(len(files)):
    for j in range(len(imageFormats)):
        if(files[i].endswith(imageFormats[j])):
            if(not os.path.isdir(imagesPath)):
                os.mkdir(imagesPath)

            if(os.path.exists(os.path.join(imagesPath, files[i]))):
                logError(files[i], imagesPath)
            else:
                shutil.move(os.path.join(downloadPath, files[i]), imagesPath)
                logMoving(files[i], imagesPath)
    
    for j in range(len(docFormats)):
        if(files[i].endswith(docFormats[j])):
            if(not os.path.isdir(docPath)):
                os.mkdir(docPath)

            if(os.path.exists(os.path.join(docPath, files[i]))):
                logError(files[i], docPath)
            else:
                shutil.move(os.path.join(downloadPath, files[i]), docPath)
                logMoving(files[i], docPath)

    for j in range(len(archiveFormats)):
        if(files[i].endswith(archiveFormats[j])):
            if(not os.path.isdir(archivePath)):
                os.mkdir(archivePath)

            if(os.path.exists(os.path.join(archivePath, files[i]))):
                logError(files[i], archivePath)
            else:
                shutil.move(os.path.join(downloadPath, files[i]), archivePath)
                logMoving(files[i], archivePath)

    for j in range(len(applicationFormats)):
        if(files[i].endswith(applicationFormats[j])):
            if(not os.path.isdir(applicationPath)):
                os.mkdir(applicationPath)

            if(os.path.exists(os.path.join(applicationPath, files[i]))):
                logError(files[i], applicationPath)
            else:
                shutil.move(os.path.join(downloadPath, files[i]), applicationPath)
                logMoving(files[i], applicationPath)
              

