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
print("Program running")

if isrunning(gygEXE):
    GYG = True
    print("Gif Your Game is running...")

while True:
    while not GYG:
        if isrunning(rlEXE):
            print("Rocket League is running...")
            print("Starting Gif Your Game")
            os.startfile(gygPATH, "open")
            sleep(3)
            os.system("cls")
            print("Gif Your Game launched successfully!")
            GYG = True
        sleep(20)
        print("Checking if Rocket League is running...")
    while GYG:
        if not isrunning(rlEXE):
            os.system("taskkill /f /im  \"Gif Your Game.exe\"")
            print("Closing Gif Your Game...")
            GYG = False
        sleep(20)
        print("Checking if Rocket League is running...")