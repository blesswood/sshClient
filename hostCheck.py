import os #bash commands (os.system())
import time #for time.sleep()
import constants

while True: #infinite check host
    bashCommand = "ping " + constants.host + " -c 5"
    try:
        os.system(bashCommand) #try to ping host
    except(RuntimeError, TimeoutError, ConnectionError): os.system("python3 startServer.py") #if error start host via startServer.py
    time.sleep(60) #wait 1 min before next check
