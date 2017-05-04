#coding=utf-8

# Y.YANG

import socket
from socket import error
import time
import queue
import threading
import logging
import os

#Library for interface
import matplotlib.pyplot as plt
import numpy as np 
import datetime as dt 
import matplotlib.dates as mdates
from datetime import datetime



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

    #threading.Thread(target=write_data_to_queue).start()
    host = "192.168.137.1"   # the server external ip, this ip should be ping success from current computer
    port = 9999
    sock = create_sock(host,port)
    while True:
        try:
            #print('receve data from'),
            #print(host)
            data = sock.recv(4096)
            print(data)
            time.sleep(1)
        except Exception as e:
            print(e)
            print('send data error...., reconnect to server ')
            print(host)

            log.error(e)
            sock = create_sock(host,port)

if __name__ == "__main__":
    start()


