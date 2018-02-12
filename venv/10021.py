#client

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('127.0.0.1', 5555))
message = 'Hello, server!'
soc.send(message.encode())

buff = []
answer = soc.recv(10024)
print(answer.decode())
soc.close()