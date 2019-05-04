# Streaming Server
import socket
import time
from random import randint

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print 'Client connection accepted ', addr
    while True:
        try:
            data = str(randint(0, 9)) + "\n"
            print 'Server sent:', data
            conn.send(data)    
        except socket.error, msg:
            print 'Client connection closed', addr
            break

conn.close()