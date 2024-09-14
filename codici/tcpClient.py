#client tcp


from socket import *

serverIP = "160.97.138.135"  #da cambiare in base al server
serverPort = 6789

#il socket di un client va indirizzato verso un ip
clientSocket = socket(AF_INET, SOCK_STREAM)		#bisogna rappresentare il tipo di socket voluto e la scelta tra tcp e udp

clientSocket.connect((serverIP, serverPort))

sentence = input("Frase : ")

inStream = clientSocket.makefile("r")
outStream = clientSocket.makefile("w")

outStream.writelines(sentence + "\n")
outStream.flush()

print("ho mandato " + sentence)

modSentence = inStream.readline()		#legge la stringa che si trova nello stream di input, quindi una frase maiuscolizzata dal server

print("DAL SERVER: " + modSentence)

clientSocket.close()