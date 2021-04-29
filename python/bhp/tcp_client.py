import socket

targetHost = "127.0.0.1"
targetPort = 80
print(targetHost)

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((targetHost, targetPort))

#send some data
message = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
#we have to encode our string using UTF-8
#client.send(message.encode("utf-8"))


#receive some data
response = client.recv(4096) #This is the amount of bytes you want to read!!

#print the response
print(response)