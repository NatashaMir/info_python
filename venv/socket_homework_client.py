#chat client

import socket
import threading
import select

class ReadThread(threading.Thread):
    def __init__(self, soc):
        threading.Thread.__init__(self)
        self.soc = soc

    #
    def run(self):
        while True:
            message = self.soc.recv(1024).decode()
            print(message)

class WriteThread(threading.Thread):
    def __init__(self, soc):
        threading.Thread.__init__(self)
        self.soc = soc

    def run(self):
        while True:
            message = input()
            self.soc.send(message.encode())

#protocol
#name:Vasya
#broadcast:Hello
#Petya:hi
#list

#connect to server
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('127.0.0.1', 7777))

#soc non block
select.select([soc],[soc],[])

#create two thread
reader = ReadThread(soc)
reader.start()

writer = WriteThread(soc)
writer.start()

reader.join()
