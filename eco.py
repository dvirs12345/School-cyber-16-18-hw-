# -*- coding: utf-8 -*-
import socket

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 1729))
my_socket.send("Hello")
print(my_socket.recv(1024))
my_socket.close()
