#server TCP


from socket import *
import os

serverPort = 6789		#importante da conoscere

welcomeSocket = socket()
welcomeSocket.bind(('', serverPort))  #con bind viene indicato su quale interfaccia ci si collega, in questo caso, lasciando vuoto, sono tutte
						#per bindare una porta inferiore a 1024 bisogna essere root

welcomeSocket.listen(2)  #oltre ad agganciarsi alla porta, si crea un buffer dimensionato sul quale ricevere chiamate

print("Server in ascolt:")

while True:
	connectionSocket, addr = welcomeSocket.accept()	
	print(addr)

	inStream = connectionSocket.makefile("r")
	outStream = connectionSocket.makefile("w")


	instruction = inStream.readline()
	print("comando = " + instruction)

	while instruction != "END":
		output = os.popen(instruction).read()
		print(output)
		
		outStream.writelines(output + "\n")	
		outStream.flush()

		instruction = inStream.readline()
		print("comando = " + instruction)

	break


print("FINE")
connectionSocket.close()