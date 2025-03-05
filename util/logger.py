from datetime import datetime
from pathlib import Path
from colorama import init,Fore,Back
init(autoreset=True)

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
            print(Fore.RED + "logs folder missing, creating folder")
            logDir.mkdir()
            print(Fore.GREEN + "created logs folder")

        if(not logFile.exists()):
            print(Fore.YELLOW + f'creating log file with name {logFileName} at {str(logFile)}')
            logFile.touch()
            print(Fore.GREEN + "created logs file")
            init = 1
    except Exception as err:
        print(Fore.BLACK + Back.RED + err)

def log(message: str, err=False):
    if(init!=1): 
        initialize()
    with logFile.open('a') as currentLog:
        currentLog.writelines(message+"\n")
        if(not err):
            print(Fore.BLUE + message)
        else:
            print(Fore.BLACK + Back.RED + message)
    
