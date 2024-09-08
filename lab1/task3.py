from sys import argv
import os

sourcePath = '.'
if len(argv) > 1:
    path = argv[1]

os.makedirs(path, exist_ok=True)

with open ('notExist.txt', 'r') as files:
    listOfFiles = files.read().splitlines()

for file in listOfFiles:
    dirPath = os.path.join(path, file)
    with open(dirPath, 'w'):
        pass