import socket
import threading
import socketserver
import threading
import json

queue_lock = threading.Lock()
message_queue = []

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def setup(self):
        print("{} connected".format(self.client_address))
        self.queue_pos = 0
    
    def to_queue(self):
        cur_thread = threading.current_thread()
        dct = json.loads(str(self.request.recv(1024), 'utf-8'))
        if 'message' in dct:
            msg = "{}: {}".format(cur_thread.name, dct)
            with queue_lock:
                message_queue.append(msg)
        elif 'type' in dct:
            print("{} is of type {}".format(cur_thread.name, dct['type']))

    def handle(self):
        while 1:
            to_queue()
            from_queue()

    def from_queue(self):
        with queue_lock:
            while queue_pos < len(message_queue):
                send(message_queue[i])
                queue_pos += 1

    def send(self, s):
        self.request.sendall(bytes(str(s), 'utf-8'))

    def finish(self):
        print("{} diconnected".format(self.client_address))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = 'localhost', 0

    server = ThreadedTCPServer((HOST,PORT), ThreadedTCPRequestHandler)
    print(server.server_address)
    server.serve_forever()
