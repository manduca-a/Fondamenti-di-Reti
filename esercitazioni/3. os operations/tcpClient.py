#client tcp


from socket import *

serverIP = "127.0.0.1"  #da cambiare in base al server
serverPort = 6789

#il socket di un client va indirizzato verso un ip
clientSocket = socket(AF_INET, SOCK_STREAM)		#bisogna rappresentare il tipo di socket voluto e la scelta tra tcp e udp

clientSocket.connect((serverIP, serverPort))


inStream = clientSocket.makefile("r")
outStream = clientSocket.makefile("w")

while True:
	command = input("Comando : ")
	

	outStream.writelines(command)
	outStream.flush()

	if command=="END":
		print("FINE")
		break

	result = inStream.readline()		#legge la stringa che si trova nello stream di input, quindi una frase maiuscolizzata dal server

	print("DAL SERVER: " + result)

clientSocket.close()