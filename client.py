import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 12345))
while True:	
	data = s.recv(1024)
	print ('Received', repr(data))
	time.sleep(1.0)