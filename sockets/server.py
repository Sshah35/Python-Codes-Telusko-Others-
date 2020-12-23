import socket  # first import the socket

s = socket.socket()           # create a socket Type of network if you want to mention
print('Socket Created')
s.bind (('localhost' , 9999))     # Bind a socket with the port. client IP since we ae working local so localhostcreate an open port
s.listen(3)                 # waiting for the client to connect so in this case 3 client in a que to connect
print('waiting for connections') # so then client is going to send a connection request so while loop

while True :
	c, addr = s.accept()               # loop here accept the the client socket request and the address
	name=c.recv(1024).decode()
	print ('connected with', addr, name)
	c.send (bytes(' Welcome now connected with Roosevelt','utf-8'))
	c.close()