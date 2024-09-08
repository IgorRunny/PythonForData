from sys import argv
import os
from shutil import copy

sourcePath = '.'
if(len(argv) > 1):
    sourcePath = argv[1]

files = os.listdir(sourcePath)
listOfSmallFiles = []

for i in files:
    fileSize = os.path.getsize(f'{sourcePath}/{i}')
    if fileSize <= 2048:
        listOfSmallFiles.append(i)

if len(listOfSmallFiles) != 0:
    try:
        os.mkdir("small")
    except:
        print("Директория была создана ранее")
    finally:
        for i in listOfSmallFiles:
            sourceFilePath = f'{sourcePath}/{i}'
            destinationFilePath = "small/" + str(i)
            copy(sourceFilePath, destinationFilePath)
else:
    print("Файлов размером меньше 2-х Кб не найдено")