import os
import sys
import datetime
from sys import argv

"""
decorator function timeSpend() calculate the time that nested function was executed
"""


def timeSpend(decoratedFunction):
    def wrapperFunction():
        start_time = datetime.datetime.now(tz=None)
        decoratedFunction()
        final_time = datetime.datetime.now(tz=None)
        print("\nВремя выполнения:" + str(final_time - start_time) + "\n")
    return wrapperFunction


"""
log files name has format: [sitename]___[guid].log
The function printSitenameList() parse file name and print sitename
If function find same sitename again, it pass this name
"""


@timeSpend
def printSitenameList():
    logDirectory = r"m:\iislogs\UNZIPED"
    # logDirectory = str((argv[0]))
    # print(str(logDirectory))
    logFiles = os.listdir(logDirectory)
    site_list = []
    for logFile in logFiles:
        name_cut_point = logFile.find("___")
        if logFile[:name_cut_point] not in site_list:
            site_list.append(logFile[:name_cut_point])
    for item in site_list:
        print(item)


printSitenameList()
