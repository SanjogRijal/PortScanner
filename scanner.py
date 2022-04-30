import sys
import socket
from datetime import datetime

if(len(sys.argv) == 2):
    target = socket.gethostbyname(sys.argv[1])
    print("Target Selected: " + target)
else:
    print("Invalid Number of Arguments")

try:
    #50-85 because most of the useful ports are covered by this much ()
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error or indicator
        if result == 0:
            print("Port {} is open".format(port))
        else:
            print("Port {} is closed".format(port))
        s.close()
except KeyboardInterrupt as e:
    print("Exiting Program {}".format(e))
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved");
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()
