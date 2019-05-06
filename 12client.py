# Dvir Sadon
import socket
import threading


def pgot():
    while True:
        print client_socket.recv(1024)


def raw():
    client_socket.send(raw_input('enter a message: \n'))


client_socket = socket.socket()


def main():
    client_socket.connect(('127.0.0.1', 8478))
    thread = threading.Thread(target=pgot)
    thread.start()
    while True:
        raw()


if __name__ == '__main__':
    main()