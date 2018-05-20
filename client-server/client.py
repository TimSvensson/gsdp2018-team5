import socket
import sys

# based on https://docs.python.org/3.4/library/socketserver.html

HOST, PORT = "localhost", 9999
data = ["one", "two", "three", "done"]

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    s = ""
    while (s != 'quit'):
    	sock.sendall(bytes(input("> ") + "\n", "utf-8"))
    	print(str(sock.recv(1024), "utf-8"))
finally:
    sock.close()