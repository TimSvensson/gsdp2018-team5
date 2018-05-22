import socket
import threading
import socketserver
import threading
import json

queue_lock = threading.Lock()
message_queue = []

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def setup(self):
        self.queue_pos = 0
        print("{} :: {} connected".format(
            threading.get_ident(), self.client_address))

    def handle(self):
        while 1:
            self.to_queue()
            self.from_queue()
            print("tid {} queue_pos {}".format(
                threading.get_ident(), self.queue_pos))
            print(message_queue)

    def finish(self):
        print("{} diconnected".format(self.client_address))



    def to_queue(self):
        dct = json.loads(str(self.request.recv(1024), 'utf-8'))
        if 'ping' in dct:
            pass
        elif 'message' in dct:
            msg = "{} :: {}".format(
                threading.get_ident(), dct)
            with queue_lock:
                message_queue.append(msg)
        elif 'type' in dct:
            print("{} is of type {}".format(
                threading.get_ident(), dct['type']))
        

    def from_queue(self):
        with queue_lock:
            if self.queue_pos < len(message_queue):
                self.send(json.dumps({'message_queue': len(message_queue), 'message': message_queue[self.queue_pos]}))
                self.queue_pos += 1

    def send(self, s):
        self.request.sendall(bytes(str(s), 'utf-8'))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = 'localhost', 0

    server = ThreadedTCPServer((HOST,PORT), ThreadedTCPRequestHandler)
    print(server.server_address)
    server.serve_forever()
