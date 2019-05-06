#Dvir Sadon
import socket
from timeit import default_timer

def main():
    """
    Add Documentation here
    """
    my_socket =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.sendto('Zain', ('127.0.0.1', 1729))
    start = default_timer()
    (data, remote_address) = my_socket.recvfrom(1024)
    duration = default_timer() - start
    print duration
    print data
    my_socket.close()

if __name__ == '__main__':
    main()