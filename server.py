import socket
import pymysql
import random

def indifiti(data):
    print('Indifini ID -', data[1])
    # data = #get, id, pass
    cursor = conn.cursor()
    #user_tbl(id VARCHAR(20) , pass VARCHAR(40));
    cursor.execute("SELECT pass FROM user_tbl WHERE id = '" + str(data[1]) + "';")
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    if str(result[0][0]) == data[2]:
        return True
    else:
        return False


def get(data,addres):
    # data = #get, id, pass
    if indifiti(data) == True:
        cursor = conn.cursor()
        #SELECT * FROM message_tbl WHERE user = '';
        cursor.execute("SELECT * FROM message_tbl WHERE user = '" + str(data[1]) + "';")
        #message_tbl(id , user VARCHAR(20) , data VARCHAR(1400) , sender VARCHAR(20)
        result = cursor.fetchall()
        for i in result:
            if i[1] == data[1]:
                message = '\033[36m{}\033[0m'.format('[' + i[3] + ']') + '\033[33m{}\033[0m'.format(i[2])
                sock.sendto(message.encode('utf-8'), addres)
                #DELETE FROM message_tbl WHERE id = 1;
                #print("DELETE FROM message_tbl WHERE id = " + i[0] + ";")
                cursor.execute("DELETE FROM message_tbl WHERE id = " + str(i[0]) + ";")
        conn.commit()
        cursor.close()
        sock.sendto('#null'.encode('utf-8'), addres)
    else:
        sock.sendto('Not Indifiti'.encode('utf-8'), addres)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5000))
print('Start Server')

conn = pymysql.connect(host='localhost',
        user='root',
        password='1234',
        db='testdb')


while True:
    data, addres = sock.recvfrom(1024)
    data = data.decode('utf-8').split(',,')
    if data[0] == '#reg': # data(#reg , pass)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM user_tbl;")
        result = cursor.fetchall()
        tmp = random.randint(0, 5000000)
        if tmp not in result:
            select = "INSERT INTO user_tbl (id, pass) VALUES ('" + str(tmp) + "'" + ", '" + str(data[1]) + "'" + ");"
            cursor.execute(select)
            conn.commit()
            cursor.close()
            sock.sendto(str(tmp).encode('utf-8'), addres)
    elif data[0] == '#get':
        get(data, addres)
    elif data[0] == '#send_to':
        print('For -', data[1], 'Text--', data[2])
        #data = #send_to, ID, text, sender
        cursor = conn.cursor()
        # INSERT INTO test_tbl (user, data,sender) VALUES ();
        cursor.execute(
            "INSERT INTO message_tbl (user, data, sender) VALUES ('" + str(data[1]) + "','" + str(data[2]) + "','" + str(data[3]) + "');")
        conn.commit()
        cursor.close()
