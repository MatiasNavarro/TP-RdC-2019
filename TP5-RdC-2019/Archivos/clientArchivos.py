#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      server.py
#
#      Copyright 2014 Recursos Python - www.recursospython.com
#
#
import socket
import time
from random import randint

def main():
    HOST = 'localhost'
    PORT = 50007

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    f = open("recibido.jpeg", "wb")
    
    while True:
        try:
            # Recibir datos del cliente.
            input_data = conn.recv(1024)
        except error:
            print("Error de lectura.")
            break
        else:
            if input_data:
                # Compatibilidad con Python 3.
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1
                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    f.write(input_data)
                else:
                    break
    
    print("El archivo se ha recibido correctamente.")
    f.close()
    
if __name__ == "__main__":
    main()