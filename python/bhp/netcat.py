#!/usr/bin/python3
import sys
import socket
import getopt
import threading
import subprocess

#define global variables
listen = False
command = False
upload = False
execute = ""
target = ""
uploadDestination = ""
port = 0

def usage():
    print ("BlackHat Python Net Tool")
    print("Usage: netcat.py -t target_host -p port")
    print("-l  --listen\t - Listen on [host]:[port] for incoming connections")
    print("-e  --execute=file_to_run\t - Execute the given file open receiving connection")
    print("-c  --command\t - initialize a command shell")
    print("-u  --upload=destination\t - Upon receiving a connection, upload file to [destination]")
    print("\n\nExamples:")
    print("""
    netcat.py -t 192.168.1.100 -p 5555 -l -c
    netcat.py -t 192.168.1.100 -p 5555 -l -u=c:\\target.exe
    netcat.py -t 192.168.1.100 -p 5555 -l -e=\"cat /etc/passwd\"
    Echo 'ABCDEFGHI' | ./netcat.py -t 192.168.1.100 -p 5555
    """)
    sys.exit(0)

def clientSender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target,port))

        if len(buffer):
            client.send(buffer)
        while True:
            recvLen = 1
            response = ""

            while recvLen:
                data = client.recv(4096)
                recvLen = len(data)
                response += data

                if recvLen  < 4096:
                    break
            print(response)

            buffer = rawInput("")
            buffer += "\n"

            client.send(buffer)
    except:
        print("[*] Exception!!  Exiting.")
        client.close()

def main():
    global listen
    global port
    global execute
    global command
    global uploadDestination
    global target

    if not len(sys.argv[1:]):
        usage()

    #read command line arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hle:t:cu:",["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(err)
        usage()

    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = True
        elif o in ("-c","--command"):
            command = True
        elif o in ("-u","--upload"):
            uploadDestination = a
        elif o in ("-t","--target"):
            target = a
        elif o in ("-p","--port"):
            port = (int)a
        else:
            assert False,"Unhandled Option"
    if not listen and len(target) and port > 0:

        buffer = sys.stdin.read()
        clientSener(buffer)

    if listen:
        serverLoop()

main()