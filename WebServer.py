#import socket module
from socket import *
import sys # In order to terminate the program

Port = 8010
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('',Port))
serverSocket.listen(10)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =   serverSocket.accept()
    try:
        message =   connectionSocket.recv(1024)
        filename = './index.html'
        f = open(filename)
        print(filename)
        outputdata = f.read()
        print(outputdata)
        #Send one HTTP header line into socket
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
        connectionSocket.send(outputdata)
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        f.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n')

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
