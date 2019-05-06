import socket

# list_of_clients = []  #not really.. only need a socket to send
list_of_sockets =[]
serversocket = socket.socket()
serversocket.bind(('127.0.0.1', 1234))
serversocket.listen(2)
# client_socket, address2 = serversocket.accept()
counter = 0
for nums in range(2):
    client_socket, address = serversocket.accept()
    # address_str = str(address)
    # index = address_str.index(',')
    # address_str = address_str[2:index-1]
    list_of_sockets.append(client_socket)


#######settimout for no spam
while True:
    serversocket.listen(2)
    # what recv??





got = client_socket.recv(int(client_socket.recv(4)))
# not_my_socket, address = serversocket.accept()

# for clients in range(len(list_of_sockets)):
#    list_of_sockets[clients].send(got)

