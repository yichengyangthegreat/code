#coding=utf-8

# version = 0.2

import socket
from socket import error
import time
import queue
import threading
import logging
import os

logging.basicConfig(level=logging.INFO,
                    filename='client.log',
                    filemode='w',
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',)
log = logging.getLogger('client')

can_msg_queue = queue.Queue(maxsize = 20)

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

3
def send_data(client,data):
    sendmsg = data  +'\r\n'
    client.send(bytes(sendmsg.encode()))


def write_data_to_queue():
    data_from_can = 'afasdfasdfasdfasdfsadfas'   # get data from can
    while True:
        try:
            can_msg_queue.put(data_from_can,block=False)
        except Exception as e:
            log.error(e)
            print(e)
            print('queue is full, clear...')
            can_msg_queue.queue.clear()
            can_msg_queue.put(data_from_can,block=False)
        time.sleep(1)



def start():



    threading.Thread(target=write_data_to_queue).start()
    host = "192.168.137.1"   # the server external ip, this ip should be ping success from current computer
    port = 9999
    sock = create_sock(host,port)
    while True:
        data = can_msg_queue.get()
        try:
            print('send data to'),
            print(host)
            send_data(sock,data)
            time.sleep(1)
        except Exception as e:
            print(e)
            print('send data error...., reconnect to server ')
            print(host)

            log.error(e)
            sock = create_sock(host,port)

if __name__ == "__main__":
    start()






