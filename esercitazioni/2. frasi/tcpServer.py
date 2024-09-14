#server TCP


from socket import *

serverPort = 6789		#importante da conoscere

welcomeSocket = socket()
welcomeSocket.bind(('', serverPort))  #con bind viene indicato su quale interfaccia ci si collega, in questo caso, lasciando vuoto, sono tutte
						#per bindare una porta inferiore a 1024 bisogna essere root

welcomeSocket.listen(2)  #oltre ad agganciarsi alla porta, si crea un buffer dimensionato sul quale ricevere chiamate

print("Server in ascolto:")

while True:
	connectionSocket, addr = welcomeSocket.accept()	#accept ritorna 2 risultati
	print(addr)

	inStream = connectionSocket.makefile("r")
	outStream = connectionSocket.makefile("w")


	clientSentence = inStream.readline()

	if clientSentence == "END":
		print("FINE")
		break

	print("Frase ricevuta: " + clientSentence)
	capitalizedSentence = clientSentence.upper()

	outStream.writelines(capitalizedSentence + "\n")	#lo \n serve perché altrimenti il server resterebbe in attesa di riceverlo e parte un wait infinito
	outStream.flush()

connectionSocket.close()