#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 50110

serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
	#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()

	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()

		connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for file not found

		print 'IOError'
		connectionSocket.send('file could not be found.')
		connectionSocket.close()
serverSocket.close()
