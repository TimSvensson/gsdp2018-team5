import socket
import threading
import socketserver
import threading
import json
import util

queue_lock = threading.Lock()
message_queue = []

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def setup(self):
        self.queue_pos = 0
        self.type = None
        print("{} :: {} connected".format(
            threading.current_thread().getName(), self.client_address))

    def handle(self):
        while 1:
            self.to_queue()
            print("{} queue_pos {} len queue {}".format(
                threading.current_thread().getName(), self.queue_pos, len(message_queue)))

    def finish(self):
        print("{} diconnected".format(self.client_address))



    def to_queue(self):
        msg = json.loads(str(self.request.recv(1024), 'utf-8'))
        print(msg)

        if msg[util._rec] == util._to_srv:
            print("_to_srv")

            if util._pop in msg[util._cont]:
                print("_pop")
                self.from_queue()

            elif util._type in msg[util._cont]:
                print("_type")
                self.type = msg[util._cont][util._type]
                print("{} is of type {}".format(
                    threading.current_thread().getName(), self.type))

        else:
            print("else")
            if util._push in msg[util._cont]:
                print("_push")
                rec = msg[util._rec]
                cont = msg[util._cont][util._push]
                msg = {rec: cont}
                with queue_lock:
                    message_queue.append(msg)

    def from_queue(self):
        with queue_lock:

            if self.queue_pos < len(message_queue):
                print("{} sending msg".format(threading.current_thread().getName()))
                msg = {util._msg: message_queue[self.queue_pos]}
                self.queue_pos += 1

            else:
                print("{} sending empty".format(threading.current_thread().getName()))
                msg = {util._empty: True}

            self.send(json.dumps(msg))

    def send(self, s):
        self.request.sendall(bytes(str(s), 'utf-8'))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = 'localhost', 0

    server = ThreadedTCPServer((HOST,PORT), ThreadedTCPRequestHandler)
    print(server.server_address)
    server.serve_forever()
