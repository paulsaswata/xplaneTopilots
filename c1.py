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
from datetime import datetime
import pytz 

'''
r_t =[] #_real,_time
v_a =[] #_Vind,_kias
v_g = [] #Vtrue,_ktgs
v_t = [] #Vtrue,_ktas
a_a = [] #hpath,__deg
w_v = [] #vpath,__deg
w_a = [] #_fuel,_1_lb
a_g = [] #_fuel,_7_lb
alpha = [] #
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


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('129.161.86.68', 8888))


#first="r_t,v_a,v_g,a_a,w_v"
first="#aoa,v" + '\r\n' 
s.sendall(first)

lineNum = 2

while True:
	lineNum += 1
	print(lineNum)
	with open('Data.txt') as csvfile:
		for skip in range(lineNum):
			next(csvfile)
		readCSV = csv.reader(csvfile, delimiter='|')
		for row in readCSV:
			#r_t=((row[0]))			
			#v_a=((row[7]))
			#v_g=((row[10]))
			v_t=((row[9]))
			a_a=((row[22]))
			w_v=((row[23]))
			alpha=((row[20]))
			csvfile.close()	
			#print(r_t,v_a,v_g,a_a,w_v,alpha)
			dt = datetime.now().isoformat()
			date =dt[:10]
			hour = dt[11:13] +"00"
			mint = dt[14:16]
			sec = dt[17:19]
			msec = dt[20:23]
			data = ":"+date+" "+ hour+mint+sec+msec+"-0500:"+alpha.strip()+','+v_t.strip()+ '\r\n'
			#data = ":"+date+" "+ hour+mint+sec+msec+"-0500:"+','+r_t.strip()+','+v_a.strip()+','+v_g.strip()+','+a_a.strip()+','+w_v.strip()+alpha.strip()
			s.sendall(data)
			print("sent", data)
			break	
	time.sleep(1.0)	        



