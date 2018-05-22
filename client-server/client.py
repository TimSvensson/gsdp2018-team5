import socket
import util
import json
import sys

client_types = "arduino", "ev3", "ui", "database", "test"

class client():
    def __init__(self, host, port, type):
        self.server = host, port
        self.type = type
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect(self.server)
        dct = {'type':self.type}
        self.send(json.dumps(dct))
                    
    def disconnect(self):
        self.sock.close()

    def send(self, str):
        self.sock.sendall(bytes(str, 'utf-8'))

    def send_obj(self, obj):
        if issubclass(obj, util.data):
            self.send(json.dumps(obj.dct_from_obj))
        else:
            print("OBJECT NOT SUBCLASS OF UTIL.DATA")

    def read(self):
        return str(self.sock.recv(1024), 'utf-8')

    def read_dct(self):
        return json.loads(self.read())

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
    c = client(HOST, PORT, client_types[4])
    try:
        c.connect()
        num_msg = 0
        while 1:
            inp = input("> ")
            if inp == "":
            	dct = {'ping': True}
            else:
            	dct = {'message': inp}
            j = json.dumps(dct)
            c.send(j)

            while 1:
            	from_serv = c.read_dct()
            	print(from_serv['message'])
            	num_msg += 1
            	if num_msg >= from_serv['message_queue']:
            		break
    finally:
        c.disconnect()
