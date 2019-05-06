# -*- coding: utf-8 -*-
#Dvir Sadon
import socket
import datetime
from random import randint

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 1729))
server_socket.listen(4)
client_socket, client_address = server_socket.accept()
got = client_socket.recv(1024)
while got != 'EXIT':
    # ends when EXIT
    if got == 'NAME':
        client_socket.send('Its uMe Mario!')
    elif got == 'RAND':
        rund = randint(1, 10)
        client_socket.send(str(rund))
    elif got == 'TIME':
        client_socket.send(str(datetime.datetime.now().time()))
    server_socket.listen(4)
    got = client_socket.recv(1024)

server_socket.close()
client_socket.close()

