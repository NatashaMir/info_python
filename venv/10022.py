#server
import socket
import threading

class SocketHandle(threading.Thread):
    def __init__(self, soc):
        threading.Thread.__init__(self)
        self.soc = soc

    def run(self):
        clientMessage = self.soc.recv(1024).decode()
        clientMessage = clientMessage + "from Server"
        self.soc.send(clientMessage.encode())
        self.soc.close()

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('0.0.0.0', 5555))
soc.listen(5)
while True:
    clienSoc, address = soc.accept()
    handle = SocketHandle(clienSoc)
    handle.start()

