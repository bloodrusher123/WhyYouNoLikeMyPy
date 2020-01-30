from datetime import datetime, timedelta, date
import time

def log(message):
    today = datetime.strftime(datetime.now(), '%d_%m_%y')
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    logFile = open("log"+today+".txt", 'a')
    logFile.write(current_time + " " + message + '\n')
    logFile.close()