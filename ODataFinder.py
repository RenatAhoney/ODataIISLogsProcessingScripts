import os
import sys
import zipfile
from datetime import datetime, date, time


logDirectory = r"m:\iislogs\MS6_unziped"
logFiles = os.listdir(logDirectory)
index = 0
filtring_start_time = datetime.today()
for logFile in logFiles:
    with open((logDirectory + "\\" + logFile), "r", encoding='UTF-8') as log:
        try:
            logStringData = log.read()
            if (logStringData.find("odata")) != -1:
                print(logFile + " ==> " + "ok")
                index += 1
                log.close()
            else:
                log.close()
                os.remove(logDirectory + "\\" + logFile)
        except Exception as ex:
            log.close()
            print("Bad Bad Log - " + logFile)
            print(ex)
filtring_finish_time = datetime.now()
print("Время начала обработки :" + str(filtring_start_time))
print("Время завершения обработки :" + str(filtring_finish_time))
print("Логов с OData: " + str(index))
print("Task is done")
