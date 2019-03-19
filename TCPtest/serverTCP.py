
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
#serverSocket.bind(('192.168.31.133',serverPort))
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)

print ("The server is ready to receive")

reply = {
	"1":"Please input lowercase sentence:",
	"2":"Please input uppercase sentence:",
}
choice = "1"
haveChoosed = False

while True:
	connectionSocket, addr = serverSocket.accept()

	message = connectionSocket.recv(1024).decode()
	
	print("Message got:\n" + message + "\n")
	
	if haveChoosed :
		if choice.isdigit():
			if int(choice) == 1:
				connectionSocket.send(message.upper().encode())
			elif int(choice) == 2:
				connectionSocket.send(message.lower().encode())
			else :
				connectionSocket.send("Error".encode())
		haveChoosed = False
		continue
	
	if message.isdigit():
		if int(message) == 1 | int(message) == 2:
			choice = message
			strM = reply[choice]
			connectionSocket.send(strM.encode())
			haveChoosed = True
			continue
	
	haveChoosed = False

connectionSocket.close()
	




