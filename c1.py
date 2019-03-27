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
r_t #_real,_time
v_a  #_Vind,_kias
v_g  #Vtrue,_ktgs
v_t  #Vtrue,_ktas
a_a  #hpath,__deg
w_v  #vpath,__deg
w_a  #_fuel,_1_lb
a_g  #_fuel,_7_lb
alpha = [] #
'''

#------client side sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
#-------------------------

#-------server side sockets
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.2', 8843))

#--------------------------


#first="r_t,v_a,v_g,a_a,w_v"
first="#aoa,v" + '\r\n' 
s.sendall(first.encode())

lineNum = 2

corrupt = False

while True:

    
	if corrupt == False:
		lineNum += 1
		print(lineNum)
		with open('Data.txt') as csvfile:
			for skip in range(lineNum):
				next(csvfile)
			readCSV = csv.reader(csvfile, delimiter='|')
			for row in readCSV:
				v_t=((row[9]))
				a_a=((row[22]))
				w_v=((row[23]))
				alpha=((row[20]))
				csvfile.close()	
				dt = datetime.now().isoformat()
				date =dt[:10]
				hour = dt[11:13] +"00"
				mint = dt[14:16]
				sec = dt[17:19]
				msec = dt[20:23]
				data = ":"+date+" "+ hour+mint+sec+msec+"-0500:"+alpha.strip()+','+v_t.strip()+ '\r\n'
				s.sendall(data.encode())
				print("sent", data)
				break
       
	time.sleep(.5)	        



