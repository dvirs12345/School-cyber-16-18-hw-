# -*- coding: utf-8 -*-
import socket
my_socket = socket.socket()
my_socket.connect(('192.168.10.91', 8844))
send_it = 'randomstring'
while send_it != 'EXIT':
    #ends when EXIT
    send_it = raw_input('wot would you like to do? ')
    while not send_it == 'NAME' and not send_it== 'RAND' and not send_it == 'EXIT' and not send_it == 'TIME':
        send_it = raw_input("and now for real ")
    my_socket.send(send_it)
    print my_socket.recv(1024)



