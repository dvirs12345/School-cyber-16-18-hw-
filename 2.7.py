# Dvir Sadon
import socket
import json
from PIL import ImageGrab
import sys


def main():
    """
    Add Documentation here
    """
    my_socket = socket.socket()
    my_socket.connect(("127.0.0.1", 8844))
    sent = raw_input('what would you like to do?')
    my_socket.send(str('0'*(4-len(str(sent))+1)) + str(len(sent)))
    my_socket.send(sent)
    while sent != 'EXIT':  # when to exit
        if sent == 'PS':
            pic_str = my_socket.recv(int(my_socket.recv(4)))
            got = pic_str
            f = open('F:/screen2.jpg', 'wb')
            while got != 'done':  # if not done
                f.write(got)
                got = my_socket.recv(int(my_socket.recv(4)))
            f.close()
        elif sent == 'LD':  # if listdir
            what = raw_input("What dir? (/wallpapers - for the wallpapers file) ")
            my_socket.send(str('0'*(4-len(str(what)))) + str(len(what)))  # sends with zeros at the start
            my_socket.send(what)
            got = my_socket.recv(int(my_socket.recv(4)))
            print json.loads(got)  # decrypts string into list
        elif sent == 'DEL':  # if delete
            got = raw_input('what would you like to delete? (full dir pls :D ) ')
            my_socket.send(str('0'*(4-len(str(got)))) + str(len(got)))
            my_socket.send(got)
        elif sent == 'MOV':  # if move
            from1 = raw_input('where would you like to copy from? (dir) ')
            my_socket.send(str('0'*(4-len(str(from1)))) + str(len(from1)))
            my_socket.send(from1)
            to = raw_input('where would you like to copy to? (dir) ')
            my_socket.send(str('0' * (4 - len(str(to)))) + str(len(to)))
            my_socket.send(to)
        elif sent == 'RUN':  # if run
            runit = raw_input('what would you like to run? (full dir pls :D) ')
            my_socket.send(str('0' * (4 - len(str(runit)))) + str(len(runit)))
            my_socket.send(runit)
        else:  # if a random string is sent
            print "Now for real!"
        sent = raw_input('what would you like to do?')
        my_socket.send(str('0' * (4 - len(str(sent)))) + str(len(sent)))
        my_socket.send(sent)

main()