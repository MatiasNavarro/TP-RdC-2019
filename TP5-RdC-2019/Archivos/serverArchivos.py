#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      client.py
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
    s.connect((HOST, PORT))
    
    while True:
        f = open("archivo.jpeg", "rb")
        content = f.read(1024)
        
        while content:
            # Enviar contenido.
            s.send(content)
            time.sleep(0.5)
            content = f.read(1024)
        
        break
    
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        s.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        s.send(bytes(chr(1), "utf-8"))
    
    # Cerrar conexión y archivo.
    s.close()
    f.close()
    print("El archivo ha sido enviado correctamente.")
if __name__ == "__main__":
    main()