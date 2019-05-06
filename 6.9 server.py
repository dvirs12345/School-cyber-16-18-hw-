# Dvir Sadon
import socket


def main():
    """
    Add Documentation here
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', 8821))
    (client_name, client_address) = server_socket.recvfrom(1024)
    server_socket.sendto(client_name, client_address)
    server_socket.close()


if __name__ == '__main__':
    main()