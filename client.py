import socket
import threading
import hashlib
import os
import time

SERVER = '127.0.0.1', 5000

def reg():
    password = input('Enter Password: ')
    hash_pass = hashlib.md5(password.encode())
    hash_pass = hash_pass.hexdigest()
    message = '#reg' + ',' + hash_pass
    sock.sendto(message.encode('utf-8'), SERVER)
    data, addres = sock.recvfrom(1024)
    return data.decode('utf-8'), hash_pass

def start():
    if os.path.exists('id.log') != True:
        id, hash_pass = reg()
        file = open('id.log', 'w')
        file.write(str(id))
        file.close()
        # '\033[31m{}\033[0m'.format() Red Text
        print('You ID# ' + '\033[31m{}\033[0m'.format(id))
        return id, hash_pass
    file = open('id.log', 'r')
    id = file.read()
    file.close()
    print('You ID# ' + '\033[31m{}\033[0m'.format(id))
    while True:
        password = input('Enter Password: ')
        hash_pass = hashlib.md5(password.encode())
        hash_pass = hash_pass.hexdigest()
        message = '#get' + ',' + id + ',' + hash_pass
        sock.sendto(message.encode('utf-8'), SERVER)
        data, addres = sock.recvfrom(1024)
        if data.decode('utf-8') == '#null':
            break
        print(data.decode('utf-8'))
    return id, hash_pass

def get():
    while True:
        message = '#get' + ',' + TITLE
        # message = #get,id,pass
        sock.sendto(message.encode('utf-8'), SERVER)
        while True:
            data, addres = sock.recvfrom(1024)
            if data.decode('utf-8') != '#null':
                print(data.decode('utf-8'))
            else:
                break
        time.sleep(30)

def send_to():
    while True:
        id_user = input('Enter ID_USER: ')
        text = input('Enter text: ')
        message = '#send_to' + ',' + id_user + ',' + text + ',' + ID
        sock.sendto(message.encode('utf-8'), SERVER)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 0))
ID, PASS = start()
TITLE = ID + ',' + PASS
potok_teg = threading.Thread(target=get)
potok_send = threading.Thread(target=send_to)
potok_teg.start()
potok_send.start()
