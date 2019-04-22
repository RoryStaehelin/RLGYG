from time import sleep
import os

def isrunning(name):
    processlist = os.popen('tasklist').readlines()
    for process in processlist:
        if name == process[:len(name)]:
            return True
    return False

rlEXE = "RocketLeague.exe"
gygEXE = "Gif Your Game.exe"
gygPATH = "C:\\Users\\Rory\\AppData\\Local\\Programs\\badpanda-react\\Gif Your Game.exe"
GYG = False

if isrunning(gygEXE):
    GYG = True

while True:
    while not GYG:
        if isrunning(rlEXE):
            os.startfile(gygPATH, "open")
            GYG = True
        sleep(20)
    while GYG:
        if not isrunning(rlEXE):
            os.system("taskkill /f /im  \"Gif Your Game.exe\"")
            GYG = False
        sleep(90)