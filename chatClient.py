import socket


my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 1234))
send_it = raw_input('what would you like to send? ')
my_socket.send(str('0' * (4 - len(str(send_it)) + 1)) + str(len(send_it)))
my_socket.send(send_it)  # maybe
len_got = my_socket.recv(4)
my_socket.recv(len_got)
