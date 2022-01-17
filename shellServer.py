from socket import *
from datetime import datetime
from sys import exit

serverPort = 8000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Listening ...")

connectionSocket, addr = serverSocket.accept()
print("Connected to " + str(addr))
message = (connectionSocket.recv(1024)).decode()
print(message)

command = ""
while (command != "exit"):
    try:
        #GET COMMAND
        command = input("$ ")
        #SEND COMMAND
        connectionSocket.send(command.encode())
        
        message = (connectionSocket.recv(1024)).decode()
        print(message)
    except:
        command = input("$ ")
connectionSocket.shutdown(SHUT_RDWR)
connectionSocket.close()
