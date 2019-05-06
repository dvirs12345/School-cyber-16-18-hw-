# Dvir Sadon
from PIL import ImageGrab
import socket
import os
import json
import shutil
import subprocess


def main():
    """
    Add Documentation here
    """
    serversocket = socket.socket()
    serversocket.bind(('127.0.0.1', 8844))
    serversocket.listen(1)
    client_socket, address = serversocket.accept()
    got = client_socket.recv(int(client_socket.recv(4)))
    while got != 'EXIT':
        if got == 'PS':  # if print screen
            im = ImageGrab.grab()
            im.save(r'F:\screen.jpg')
            pic = open('F:\screen.jpg', 'rb')  # print screen
            k = pic.read(1024)
            while k:  # cutting into pieces
                length = len(k)
                # print client_socket.send(str('0'*(4-len(str(k)))) + str(length))
                print str(len(k)).zfill(4)
                client_socket.send(str(str(len(k)).zfill(4)))
                #client_socket.send(str('0'*(4-len(str(k)))) + str(length))  # ##############
                # print str('0'*(1024-len(str(k))+1)) + str(k)
                client_socket.send(k)
                k = pic.read(1024)
            client_socket.send('0004')
            client_socket.send('done')  # confirm done
        if got == 'LD':  # if listdir
            what = client_socket.recv(int(client_socket.recv(4)))
            my_list = os.listdir(what)  # list of filenames
            after = json.dumps(my_list)
            client_socket.send(str('0'*(4-len(str(after)))) + str(len(after)))
            client_socket.send(after)
            print json.loads(after)
        if got == 'DEL':  # if delete
            delit = client_socket.recv(int(client_socket.recv(4)))
            os.remove(delit)  # removes
        if got == 'MOV':  # if move
            sorse = client_socket.recv(int(client_socket.recv(4)))
            dest = client_socket.recv(int(client_socket.recv(4)))
            if os.path.exists(sorse) and os.path.exists(dest):  # if exists
                shutil.copy2(sorse, dest)
        if got == 'RUN':  # if run
            bolt = client_socket.recv(int(client_socket.recv(4)))
            # if os.path.exists(bolt):
            os.startfile(bolt)  # runs the file
        got = client_socket.recv(int(client_socket.recv(4)))


main()
