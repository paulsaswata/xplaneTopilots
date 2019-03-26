import socket
import time


#host = '127.0.0.1'  # standard localhost
host = '129.161.86.68'
port = 8888     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print (host , port)
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

while True:	
	data = s.recv(1024)
	print ('Received', repr(data))
	time.sleep(1.0)