import socket
targetHost = "127.0.0.1"
targetPort = 80

#create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
message = "AAAABBBBCCCCDDDD"
client.sendto(message.encode("utf-8"), (targetHost, targetPort))

#receive data
data, addr = client.recvfrom(4096)

ptint(data)