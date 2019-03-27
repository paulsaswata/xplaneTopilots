import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))

print ("started listening at 127.0.0.1, 8888 ")
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

while True:
	print ("--")
	data = conn.recv(1024)
	print ('Received', repr(data))
	time.sleep(1.0)