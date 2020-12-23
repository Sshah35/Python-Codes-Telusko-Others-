import socket

c = socket.socket()

c.connect(('localhost', 9999))

name = input('Please enter your name :')
c.send(bytes(name,'utf-8'))
# message is received initial as an byte we need to decode
print(c.recv(1024).decode())


