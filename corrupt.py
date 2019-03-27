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

import sys
from select import select

timeout = 0.5
#------client side sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.2', 8843))
#-------------------------

inject = ''

s.sendall(inject.encode())

