import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def setup(self):
        print("{} connected".format(self.client_address))
    
    def handle(self):
        while 1:
            data = str(self.request.recv(1024), 'utf-8')
            cur_thread = threading.current_thread()
            response = bytes("{}: {}".format(cur_thread.name, data), 'utf-8')
            print(str(response))
            self.request.sendall(response)

    def finish(self):
        print("{} diconnected".format(self.client_address))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = 'localhost', 0

    server = ThreadedTCPServer((HOST,PORT), ThreadedTCPRequestHandler)
    print(server.server_address)
    server.serve_forever()
