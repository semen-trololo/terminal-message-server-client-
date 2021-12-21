import socket
import threading
import hashlib
import os
import random
import time

SERVER = '127.0.0.1', 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 0))

def login():
        password = input('Enter Password: ')
        hash_pass = hashlib.md5(password.encode())
        hash_pass = hash_pass.hexdigest()
        del password
        return hash_pass
def get():
    while 1:
        message = '#get' + ',' + TITLE
        sock.sendto(message.encode('utf-8'), SERVER)
        while 1:
            data, addres = sock.recvfrom(1024)
            if data.decode('utf-8') == '#null':
                flag = False
                break
            print(data.decode('utf-8'))
        time.sleep(30)
def start():
        if os.path.exists('id2.log') != True:
                tmp = random.randint(0, 5000000)
                file = open('id2.log', 'w')
                file.write(str(tmp))
                file.close()
        file = open('id2.log', 'r')
        id = file.read()
        file.close()
        print('You ID#' + id)
        return id
def send_to():
    while 1:
        id_user = input('Enter ID_USER: ')
        text = input('Enter text: ')
        message = '#send_to' + ',' + TITLE + ',' + id_user + ',' + text
        sock.sendto(message.encode('utf-8'), SERVER)
ID = start()
PASSWORD = login()
TITLE = ID + ',' + PASSWORD
potok = threading.Thread(target=get)
potok1 = threading.Thread(target=send_to)
potok.start()
#potok1.start()