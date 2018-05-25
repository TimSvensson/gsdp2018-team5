import socket
import threading
import socketserver
import threading
import json
import util
import socket
import struct

DEBUG = False

queue_lock = threading.Lock()
msg_q = []

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def setup(self):
        self.q_pos = 0
        self.type = None
#        print("{} :: {} connected".format(
#            threading.current_thread().getName(), self.client_address))

    def handle(self):
        self.loop = True
        while self.loop:
            self.to_queue()
            print("{} q_pos {} len queue {}".format(
                threading.current_thread().getName(), self.q_pos, len(msg_q)))

    def finish(self):
        print("{} diconnected".format(self.client_address))



    def to_queue(self):
        try:
            s = str(util.recv_msg(self.request), 'utf-8')
            msg = json.loads(s)
            print("read {} {} {}".format(threadding.current_thread().getName(), self.type,msg))

            if util._pop in msg:
                print("_pop")
                self.from_queue()

            elif util._push in msg:
                print("_push")
                
                if msg[util._rec] == util._to_srv:
                    print("_to_srv")
                    if util._type in msg:
                        print("_type")
                        self.type = msg[util._type]
                else:
                    with queue_lock:
                        msg_q.append(msg)
            else:
                print("else")
        except:
            self.loop = False
            
    def from_queue(self):
        with queue_lock:

            msg = ''
            while msg == '':
                if self.q_pos < len(msg_q):
                    if self.type == msg_q[self.q_pos][util._rec] or msg_q[self.q_pos][util._rec] == util._to_all:
#                       print("{} sending msg".format(threading.current_thread().getName()))
                        msg = {util._msg: msg_q[self.q_pos]}
                    self.q_pos += 1

                else:
#                    print("{} sending empty".format(threading.current_thread().getName()))
                    msg = {util._empty: True}

            print(msg)
            self.send(json.dumps(msg))

    def send(self, msg):
        print("send {} {} {}".format(threadding.current_thread().getName(), self.type, msg))
        util.send_msg(self.request, bytes(str(msg), 'utf-8'))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = 'localhost', 0

    server = ThreadedTCPServer((HOST,PORT), ThreadedTCPRequestHandler)
    print(server.server_address)
    server.serve_forever()
