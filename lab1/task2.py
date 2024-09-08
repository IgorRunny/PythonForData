import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dirpath', default = '.' )
parser.add_argument('--files', nargs = '*', default='')

parseArgs = parser.parse_args()
sourcePath = parseArgs.dirpath
files = parseArgs.files

existFiles =[]
notExistFiles = []
dirFiles = os.listdir(sourcePath)

if len(files) != 0:
    for file in files:
        check = False
        for exist in dirFiles:
            if file == exist:
                check = True
                break
        if check:
            existFiles.append(file)
        else:
            notExistFiles.append(file)

    with open('exist.txt', 'w') as exist, open('notExist.txt', 'w') as notExist:
        print('exist files:')
        for i in existFiles:
            print(f'{i}')
            exist.write(f'{i}\n')

        print('not exist files:')
        for i in notExistFiles:
            print(f'{i}')
            notExist.write(f'{i}\n')
else:
    numOfFiles = len(dirFiles)
    sum = 0
    for i in dirFiles:
        sum += os.path.getsize(f'{sourcePath}/{i}')
    print(f'В директории {numOfFiles} файла(ов) общим размером {sum} байт')
