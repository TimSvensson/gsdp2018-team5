import socketserver
import util
import json
import sys

# based on https://docs.python.org/3.4/library/socketserver.html

class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = None
        while self.data != 'quit':
            self.data = self.request.recv(1024).strip()
            print("{}:{} wrote:".format(self.client_address[0],self.client_address[1]))
            print(str(self.data))
            self.request.sendall(self.data.upper())

def show_help():
    print("Usage:")
    print("\t-h | --help\tDisplay help")
    print("\t-p | --port\tSelect port to use, default: 9999")
    print("\t-H | --host\tHost address to use, default: localhost")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    for i in range(len(sys.argv)):
        if (i != 0):
            a = sys.argv[i]
            if   (a=="-p" or a=="--port"):
                PORT = int(sys.argv[i+1])
            elif (a=="-H" or a=="--host"):
                HOST = sys.argv[i+1]
            elif (a=="-h" or a=="--help"):
                show_help()
                exit(0)

    server = socketserver.TCPServer((HOST, PORT), Handler)
    server.serve_forever()