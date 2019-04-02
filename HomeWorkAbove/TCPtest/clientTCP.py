
from socket import *

#serverName = '192.168.31.133'
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

receiveMessage = "nothing"
while True:
	if receiveMessage == "nothing":
		print("Welcome! What can I do for you？\n1.To uppercase\n2.To lowercase\n3.exit")
		choice = input()
		if int(choice) == 3:
			break
		clientSocket.send(choice.encode())
		receiveMessage = clientSocket.recv(1024)
		print("From Server:\n", receiveMessage.decode())
	sendMessage = input()
	clientSocket.send(sendMessage.encode())
	
	modifiedSentence = clientSocket.recv(1024)
	print("From Server:", modifiedSentence.decode())


clientSocket.close()

