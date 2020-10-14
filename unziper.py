# Берет из папки с логами их архивых, и распаковывает в указанную папку
# После распаковки из-за того, что архивы могут содержать одноименные файлы
# переименовывает их путем добавления в название файла UUID
import os
import sys
import zipfile
import uuid
import datetime
from sys import argv


# logArchiveDirectory = r'm:\iislogs\MS1'
# logDirectory = r"m:\iislogs\MS1UNZIP"
logArchiveDirectory = r"m:\iislogs\UA2"
tempDirectory = r"m:\iislogs\Temp"
logDirectory = r"m:\iislogs\UNZIPED"
files = os.listdir(logArchiveDirectory)
index = 0
start_time = datetime.datetime.now(tz=None)

archivFiles = []
for item in files:
    if item.endswith(".zip"):
        archivFiles.append(item)

for archive in archivFiles:
    log = zipfile.ZipFile(logArchiveDirectory + "\\" + archive)
    filesInArchive = log.namelist()
    for file in filesInArchive:
        log.extract(file, tempDirectory)
        items = os.listdir(tempDirectory)
        file_name_cut_point = archive.find("-Logs")
        for item in items:
            newItemName = archive[:file_name_cut_point] + "___" + str(uuid.uuid1()) + ".log"
            os.rename(tempDirectory + "\\" + item,
                      logDirectory + "\\" + newItemName)
            print(str(index) + ":\t" + archive)
            index +=1
finish_time = datetime.datetime.now(tz=None)
print("Количество файлов: " + str(index))
print("Продолжительность обработки:"  + str(finish_time - start_time))
