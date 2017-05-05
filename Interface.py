#coding=utf-8
# Y.YANG
# Bhisan Saraye

import socket
from socket import error
import time
import queue
import threading
import logging
import os


#Library for interface
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
from datetime import datetime
from threading import *
import re
import sched, time


logging.basicConfig(level=logging.INFO,
                    filename='client.log',
                    filemode='w',
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',)
log = logging.getLogger('client')


def create_sock(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    while True:
        try:
            sock.connect((host, port))
            break
        except error as e:
            log.error(e)
            print(e)
            print('wait 5 seconds, reconnect again...')
            log.error('wait 5 seconds, reconnect again...')
            time.sleep(5)
    return sock



def start():
    host = "172.23.82.101"
    # the server external ip, this ip should be ping success from current computer
    port = 9999
    sock = create_sock(host,port)
    while True:
        try:
            print('receve data from'),
            print(host)
            data = sock.recv(4096)
            #time.sleep(1)
            
        except Exception as e:
            print(e)
            print('send data error...., reconnect to server ')
            print(host)

            log.error(e)
            sock = create_sock(host,port)


        q.put(data)
        
        if q.empty() != True:
            message = q.get()
            data = str(message, 'utf-8')
            new_data= re.sub('\; \r\n','', data)
            graph_data.append(new_data)
            print(new_data)

        print(graph_data)
        # Look Up table
        Speed          = '513.0'
        Temperature   = '1025'
        torque_control = '514'

        #List to store data of the senso
        Temperature_data = []
        Speed_data       = []
        Torque_data      = []

        for line in graph_data:
            if (Temperature in line):
                Temperature_data.append(line)
            elif(Speed in line):
                Speed_data.append(line)
            elif(torque_control in line):
                Torque_data.append(line)

        Time1=[]
        data1 =[]

        Time2 =[]
        data2= []

        Time3=[]
        data3=[]

        for line in Temperature_data:
            Time1, ID1, data1 = np.loadtxt(Temperature_data, delimiter =',', unpack= True)

        for line in Speed_data:
            Time2, ID2 , data2 = np.loadtxt(Speed_data, delimiter =',', unpack = True)

        #for line in Torque_data:
        #    Time3, ID3 , data3 = np.loadtxt(Torque_data, delimiter =',', unpack = True)

        print(Time1)
        print(data1)
        #plt.subplot(221)
        #plt.plot(Time3, data3)
        #plt.ylabel('Position Sensor')
        #plt.xlabel('Time')

        plt.subplot(211)
        plt.plot(Time1,data1)
        plt.ylabel('Temperature ')

        plt.subplot(212)
        plt.plot(Time2, data2)
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency')
        plt.draw()
        plt.pause(.1)

def rec():
    host = "192.168.1.100"   # the server external ip, this ip should be ping success from current compute
    port = 9999
    sock = create_sock(host,port)
    while True:
        message = sock.recv(4096)
        q.put(message)			# Add to message queue

q = queue.Queue()			# Define Queue	
t = Thread(target = rec)		# Start rx thread
t.start()
graph_data = []
Time1=[]
data1=[]


plt.ion()
ax1= plt.axes()


line = plt.plot([], [])

if __name__ == '__main__':

    start()
