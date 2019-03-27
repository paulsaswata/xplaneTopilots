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
import threading
import random

''' variables and their Xplane counterparts
r_t #_real,_time, v_a  #_Vind,_kias, v_g  #Vtrue,_ktgs, v_t  #Vtrue,_ktas, a_a  #hpath,__deg, w_v  #vpath,__deg, w_a  #_fuel,_1_lb, a_g  #_fuel,_7_lb, alpha #
'''

#debug = True shows print statements for debugging
DEBUG = False

#enter error to inject here
INJECT_ERROR = (100 + random.uniform(-.5,.5))

CORRECT_FLAG = True
def tcpClient():
	#client side socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', 8888)) #address of where pilots server is listening
	first="#aoa,v" + '\r\n' 
	s.sendall(first.encode())
	lineNum = 2
	while True:
		lineNum += 1
		print('\n',lineNum)
		if CORRECT_FLAG == False:
			if DEBUG: print("ERROR MODE!")    
			error = INJECT_ERROR
		else:
			if DEBUG: print("Normal Mode.")
			error = 1

		with open('Data.txt') as csvfile:
			for skip in range(lineNum):
				next(csvfile)
			readCSV = csv.reader(csvfile, delimiter='|')
			for row in readCSV:
				v_t=(float((row[9]).strip()))
				a_a=(float((row[22]).strip()))
				w_v=(float((row[23]).strip()))
				alpha=(float((row[20]).strip())) * error #error added to alpha 
				csvfile.close()	
				dt = datetime.now().isoformat()
				date =dt[:10]
				hour = dt[11:13] +"00"
				mint = dt[14:16]
				sec = dt[17:19]
				msec = dt[20:23]
				data = ":"+date+" "+ hour+mint+sec+msec+"-0500:"+str(alpha)+','+str(v_t)+ '\r\n'
				s.sendall(data.encode())
				if DEBUG:print("sent", data)
				break	       
			time.sleep(1.0)	        

def errorInjector():
	global CORRECT_FLAG
	while True:
		inp = input()
		if inp == 1:
			CORRECT_FLAG = False
		else:
			CORRECT_FLAG = True


thread1 = threading.Thread(target=tcpClient)
thread2 = threading.Thread(target=errorInjector)

thread1.start()
thread2.start()