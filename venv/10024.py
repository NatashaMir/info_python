#chat server

import socket
import threading

class SocketHandle(threading.Thread):
    def __init__(self, soc, dict):
        threading.Thread.__init__(self)
        self.soc = soc
        self.dict = dict

    def run(self):
        while True:
            message = self.soc.recv(1024).decode()
            messArray = message.split(':')
            if messArray[0] == 'name':
                self.dict[messArray[1]] = self.soc
            elif messArray[0] == 'broadcast':
                for clientSocket in self.dict.values():
                    clientSocket.send(messArray[1].encode())
            elif messArray[0] == 'list':
                outputMess = ''
                for name in self.dict.keys():
                    outputMess += name + '\n'
                self.soc.send(outputMess.encode())
            else:
                toName = messArray[0]
                for key, value in  self.dict.items():
                    if value == self.soc:
                        fromName = key
                        break
                mess = fromName + ':' + messArray[1]
                self.dict[toName].send(mess.encode())


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('0.0.0.0', 7777))
soc.listen(5)
dict = {}
while True:
    clienSoc, address = soc.accept()
    handle = SocketHandle(clienSoc, dict)
    handle.start()