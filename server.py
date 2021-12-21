import socket
import pymysql

conn = pymysql.connect(host='localhost',
        user='root',
        password='1234',
        db='testdb')

USERS = []
MESSAGE = [['111', '2342', 'test']]
def get(data,addres):
    flag = False
    cursor = conn.cursor()
    #SELECT * FROM message_tbl WHERE user = '12';
    cursor.execute("SELECT * FROM message_tbl WHERE user = '" + str(data[1]) + "';")
    result = cursor.fetchall()
    for i in result:
        if i[1] == data[1]:
            sock.sendto(i[2].encode('utf-8'), addres)
            #DELETE FROM message_tbl WHERE id = 1;
            #print("DELETE FROM message_tbl WHERE id = " + i[0] + ";")
            cursor.execute("DELETE FROM message_tbl WHERE id = " + str(i[0]) + ";")
            flag = True
            continue

    sock.sendto('#null'.encode('utf-8'), addres)
    conn.commit()
    cursor.close()
def indifiti(data):
    flag = False
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM user_tbl;")
    result = cursor.fetchall()
    for i in result:

        if data[1] == i[0]:
            print('Есть клиент')
            flag = True
    cursor.execute("SELECT * FROM user_tbl;")
    result = cursor.fetchall()

    for i in result:
        if flag == True:

            if i[0] == data[1]:
                if i[1] == data[2]:
                    print('User ind ', i[0])
                    return True
                else:
                    print('User not ind')
                    return False
    cursor.execute("INSERT INTO user_tbl (id, pass) VALUES ('" + str(data[1]) +"'" + ", '" + str(data[2]) + "'" + ");")
    conn.commit()
    cursor.close()
    #conn.close()
    #print('User Add', data[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5000))
print('Start Server')
while 1:
         data, addres = sock.recvfrom(1024)
         data = data.decode('utf-8').split(',')
         if indifiti(data) == False:
             sock.sendto('Not Indifiti'.encode('utf-8'), addres)
             continue
         if data[0] == '#get':
             print('get')
             get(data, addres)
         elif data[0] == '#send_to':
             print(data[3], data[4])
             cursor = conn.cursor()
             #INSERT INTO test_tbl (user, pass, data) VALUES ('root', '12345', '2019-11-24');
             cursor.execute("INSERT INTO message_tbl (user, data) VALUES ('" + str(data[3]) + "'" + "," + "'" + str(data[4]) + "');")
             conn.commit()
             cursor.close()
             #MESSAGE.append(['[' +str(data[1]) + ']', data[3], data[4]])
