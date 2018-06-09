import socket
import sys
from datetime import datetime

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)


print("-" * 40)
print("begun scanning on: ", remoteServerIP)
print("-" * 40)

t1 = datetime.now()


try:
    for port in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:   Open".format(port))
        sock.close()

except socket.gaierror:
    sys.exit("Hostname could not be resolved. Exiting")

except socket.error:
    sys.exit("Could not connect to server")


t2 = datetime.now()

totalTime = t2 - t1

print("Scanning completed in: ", totalTime)