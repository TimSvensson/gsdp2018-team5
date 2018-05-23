import socket
import util
import json
import sys

class client():
    def __init__(self, host, port, type):
        self.server = host, port
        self.type = type
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect(self.server)

        dct = {util._type: self.type}
        self.send_to(util._to_srv, dct)
                    
    def disconnect(self):
        self.sock.close()

    def send(self, str):
        self.sock.sendall(bytes(str, 'utf-8'))

    def str_from_obj(self, obj):
        if issubclass(obj, util.data):
            return str(json.dumps(obj.dct_from_obj))
        else:
            return None

    def send_to(self, recepient, content):
        self.send(str(json.dumps(
            {util._rec: recepient, util._cont: content})))

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
    c = client(HOST, PORT, util._test)
    try:
        c.connect()
        while 1:
            inp = input("> ")
            
            if (inp == ""):

                c.send_to(util._to_srv, util._pop)
                from_serv = c.read_dct()
                
                if util._empty in from_serv:
                    print("End of message queue")
                elif util._msg in from_serv:
                    print(from_serv[util._msg])

            else:
                msg = {util._push: inp}
                c.send_to(util._to_all, msg)
    finally:
        c.disconnect()
