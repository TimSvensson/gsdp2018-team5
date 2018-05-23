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
        self.send(util._to_srv, dct)
                    
    def disconnect(self):
        self.sock.close()



    # push / pop :: server / client
    def __push(self, dct):
        s = str(json.dumps(dct))
        print(s)
        util.send_msg(self.sock, (bytes(s, 'utf-8')))

    # recv: recv, _push: true, _cont: cont
    def send(self, recepient, dct):
        dct.update({util._rec: recepient})
        dct.update({util._push: True})
        self.__push(dct)

    # recv: to_serv, _pop: True
    def read(self):
        pop = {util._rec: util._to_srv, util._pop: True}
        self.__push(pop)
        return json.loads(str(util.recv_msg(self.sock), 'utf-8'))



t_ard1 = util.ard_to_dct(1,2)
t_ard2 = util.ard_to_dct(15,12)

t_ev3_s = util.ev3_status_to_dct('abc', 5)

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
    c = client(HOST, PORT, util._ard)
    try:
        c.connect()
        first = True
        while 1:
        
            if first == True:
                c.send(util._ard, t_ard1)
                c.send(util._ard, t_ard2)
                c.send(util._db, t_ev3_s)
            
            inp = input("> ")

            if (inp == ""):

                #c.push(util._to_srv, util._pop)
                from_serv = c.read()
                
                if util._empty in from_serv:
                    print("EOQ")
                elif util._msg in from_serv:
                    print(from_serv[util._msg])

            else:
                msg = {util._msg: inp}
                c.send(util._to_all, msg)

            first = False
    finally:
        c.disconnect()
