import socket
import threading

bindIP = "0.0.0.0"
bindPort = 9999

#create the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Open the sever
server.bind((bindIP, bindPort))

#Listen for connections
server.listen(5)
print("Listening on %s:%d" %(bindIP,bindPort))

#This is the client handling thread
def handleClient(clientSocket):
    #print out what the client saends
    request = clientSocket.recv(1024)

    print(f"[*] Received: ${request}")

    #send back data
    quitMSG = "ACK!"
    clientSocket.send(quitMSG.encode("utf-8"))

    #Close the connection
    clientSocket.close()

while True:

    clientAddr = server.accept()

    print (f"[*] Accepted connecction from {clientAddr}")

    clientHandler = threading.Thread(target=handleClient,args=(clientAddr,))
    clientHandler.start()