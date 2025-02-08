from datetime import datetime
from pathlib import Path

######
FILE_FORMAT = "bot_log_%H-%M-%S_%d-%m-%y.log"
LOGDIR = "./logs/"
######


logFileName = datetime.now().strftime(FILE_FORMAT)
logDir = Path(LOGDIR)
logFile = logDir.joinpath(logFileName)
init = 0
def initialize():
    try:
        global init
        global logFileName
        global logDir
        global logFile
        if(not logDir.exists()): 
            print("logs folder missing, creating folder")
            logDir.mkdir()
            print("created logs folder")

        if(not logFile.exists()):
            print(f'creating log file with name {logFileName} at {str(logFile)}')
            logFile.touch()
            print("created logs file")
            init = 1
    except Exception as err:
        print(err)

def log(message: str):
    if(init!=1): 
        initialize()
    with logFile.open('a') as currentLog:
        currentLog.writelines(message+"\n")
        print(message)
