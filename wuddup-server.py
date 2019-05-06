# Dvir Sadon
import socket
import select

PORT = 8478
messages_to_send = []
managers = []
managers.append("dvir")


def send_waiting_messages(wlist):
    for message in messages_to_send:
        (client_socket1, data) = message
        for clint in wlist:
            if clint is not client_socket1:
                clint.send(data)
        messages_to_send.remove(message)


def main():  # 395
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', PORT))
    server_socket.listen(5)
    open_client_sockets = []
    while True:
        rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                (new_socket, address) = server_socket.accept()
                open_client_sockets.append(new_socket)
            else:
                clientN = current_socket.recv(1024)
                data = current_socket.recv(1024)
                if data == "has left the server":
                    messages_to_send.append((current_socket, clientN + ": " + data))
                    send_waiting_messages(wlist)
                elif data == "":
                    open_client_sockets.remove(current_socket)
                    print "Connection with client closed"
                else:
                    messages_to_send.append((current_socket, clientN+": "+data))
        send_waiting_messages(wlist)


main()
