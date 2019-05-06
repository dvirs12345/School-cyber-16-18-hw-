# -*- coding: utf-8 -*-
'''
220 mail.gmx.com GMX Mailservices ESMTP {mp-eu002}
EHLO  ####
250-mail.gmx.com GMX Mailservices
250-8BITMIME
250-ENHANCEDSTATUSCODES
250-SIZE
250-AUTH=LOGIN PLAIN
250-AUTH LOGIN PLAIN
250 STARTTLS
AUTH PLAIN AGZydXN0YUBnbXguY29tAFBhc3N3b3JkMSE= #####
235 2.7.0 Go ahead {mp-eu002}
MAIL FROM:<frusta@gmx.com> ####
250 2.1.0 ok {mp-eu002}
RCPT TO:resha@bads.com  ####
250 2.1.5 ok {mp-eu002}
DATA ####
354 mail.gmx.com Go ahead {mp-eu002}
Subject: Get Ready! ###

Be ready for the attack.
Make sure that everything in place.
It's going to be fun!
Yours, Frusta
.
250 2.6.0 Message accepted {mp-eu002}
QUIT ###
221 2.0.0 GMX Mailservices {mp-eu002}
'''
import socket


def send_And_recieve():
    my_socket = socket.socket()
    my_socket.connect(('networks.cyber.org.il', 587))
    user = raw_input("enter your username ")
    password = raw_input("enter your password ")
    encoded = ('\x00' + user + '\x00' + password).encode('base64')
    x1 = my_socket.recv(1024)
    my_socket.send('EHLO\r\n')
    x2 = my_socket.recv(1024)
    my_socket.send('AUTH PLAIN ' + encoded+'\r\n')
    x3 = my_socket.recv(1024)
    my_socket.send('MAIL FROM:<' + user + '>'+'\r\n')
    x4 = my_socket.recv(1024)
    send_to = raw_input('enter the person you want to send to')
    my_socket.send('RCPT TO:'+send_to+'\r\n')
    x5 = my_socket.recv(1024)
    my_socket.send('DATA\r\n')
    x6 = my_socket.recv(1024)
    subject = raw_input('enter the subject')
    data = raw_input('enter the data')
    my_socket.send('Subject: '+subject+'\r\n'+'\r\n'+data+'\r\n'+'.'+'\r\n')
    x7 = my_socket.recv(1024)
    my_socket.send('QUIT\r\n')
    x8 = my_socket.recv(1024)
    print x8


def main():
    send_And_recieve()


if __name__ == '__main__':
    main()