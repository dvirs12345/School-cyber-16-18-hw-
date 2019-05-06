#Dvir Sadon
import socket


def main():
    """
    Add Documentation here
    """
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.sendto('Omer', ('1.2.3.4', 8821))
    (data, remote_address) = my_socket.recvfrom(1024)
    print data
    my_socket.close()


if __name__ == '__main__':
    main()