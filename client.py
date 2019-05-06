# -*- coding: utf-8 -*-
import PIL
import socket


mysocet = socket.socket()
mysocet.connect(('127.0.0.1', 8820))
mysocet.send('awsome')
print(mysocet.recv(1024))
mysocet.close()
