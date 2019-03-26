import socket
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import time
import os
from itertools import islice

'''
r_t =[] #_real,_time
v_a =[] #_Vind,_kias
v_g = [] #Vtrue,_ktgs
a_a = [] #hpath,__deg
w_v = [] #vpath,__deg
w_a = [] #_fuel,_1_lb
a_g = [] #_fuel,_7_lb
'''

'''
while True:
	lineNum += 1
	with open('Data.txt') as csvfile:
		readCSV = csv.reader(csvfile, delimiter='|')
		print(lineNum)
		for row in islice(readCSV, lineNum, None):
			r_t.append(float(row[0]))			
			v_a.append(float(row[7]))
			v_g.append(float(row[10]))
			a_a.append(float(row[22]))
			w_v.append(float(row[23]))	
			print(r_t[0],v_a[0],v_g[0],a_a[0],w_v[0])
			break
	        #w_a.append(float(row[0])) 
	        #a_g.append(float(row[0]))
	csvfile.close()
	time.sleep(1.0)
'''
'''
#works
lineNum = 2

while True:
	lineNum += 1
	print(lineNum)
	with open('Data.txt') as csvfile:
		for skip in range(lineNum):
			next(csvfile)
		readCSV = csv.reader(csvfile, delimiter='|')
		for row in readCSV:
			r_t=(float(row[0]))			
			v_a=(float(row[7]))
			v_g=(float(row[10]))
			a_a=(float(row[22]))
			w_v=(float(row[23]))
			csvfile.close()	
			print(r_t,v_a,v_g,a_a,w_v)
			break	
	time.sleep(1.0)	        

'''



host = '127.0.0.1'  # standard localhost
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print host , port
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

first="r_t,v_a,v_g,a_a,w_v" 
conn.sendall(first)

lineNum = 2

while True:
	lineNum += 1
	print(lineNum)
	with open('Data.txt') as csvfile:
		for skip in range(lineNum):
			next(csvfile)
		readCSV = csv.reader(csvfile, delimiter='|')
		for row in readCSV:
			r_t=((row[0]))			
			v_a=((row[7]))
			v_g=((row[10]))
			a_a=((row[22]))
			w_v=((row[23]))
			csvfile.close()	
			print(r_t,v_a,v_g,a_a,w_v)
			data = ":2013-05-11 140001000-0500:"+','+r_t.strip()+','+v_a.strip()+','+v_g.strip()+','+a_a.strip()+','+w_v.strip()
			conn.sendall(data)
			break	
	time.sleep(1.0)	        

