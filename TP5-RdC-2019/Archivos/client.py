#  Streaming Client

import socket
import time

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
a=0.5
# cont = 0

while True:
    data = s.recv(1024)
    time.sleep(a)
    print data

    # cont = cont +1
    # print "cont: ",cont
    # if(cont == 10):
    #     print "Time: ", a
    #     a = 0.75
    # elif(cont == 20):
    #     a = 1.0
    #     print "Time: ", a
    # elif(cont == 30):
    #     a = 1.5
    #     print "Time: ", a
    # elif(cont == 40):
    #     a = 2.0
    #     print "Time: ", a
    # elif(cont == 50):
    #     a = 2.0
    #     cont = 0
    #     print "Time: ", a       

s.close()