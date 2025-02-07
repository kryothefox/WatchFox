import psutil,os

def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def getSystemInfo():
    systemdata = {
        "CPU Usage (%)" : f"{psutil.cpu_percent()}%",
        "Memory Usage (System)" : f"{round((psutil.virtual_memory()[0]-psutil.virtual_memory()[1])/1000000000,2)}GB used out of {round(psutil.virtual_memory()[0]/1000000000,2)}GB",
        "Memory Usage (Process)" : f"{round(process_memory()/1000000)}MB",
    }
    #### LOADS OF ZEROES AAAAA TWTTTTTT 
    return systemdata