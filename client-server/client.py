import socket
import sys

class client():
    def __init__(self, host, port):
        self.server = host, port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect(self.server)
                    
    def disconnect(self):
        self.sock.close()

    def send(self, str):
        self.sock.sendall(bytes(str, 'utf-8'))

    def read(self):
        return str(self.sock.recv(1024), 'utf-8')

HOST, PORT = 'localhost', 9999
if __name__ == "__main__":

    # Check for right type of arguments
    if (len(sys.argv) > 1):
        PORT = int(sys.argv[1])
    if (len(sys.argv) == 3):
        HOST = sys.argv[2]
    if (len(sys.argv) > 3):
        sys.exit(1)

    # Start client
    c = client(HOST, PORT)
    try:
        c.connect()
        while 1:
            msg = input("> ")
            c.send(msg)
            print(c.read())
    finally:
        c.disconnect()
