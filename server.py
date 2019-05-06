# Dvir Sadon
import socket
import cv2
import numpy

"""
UDP_IP = "127.0.0.1"
UDP_PORT = 8389

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
s = ""
while True:
    data, addr = sock.recvfrom(46080/5)
    s += data
    if len(s) == (46080 * 20):
        frame = numpy.fromstring(s, dtype=numpy.uint8)
        frame = frame.reshape(480, 640, 3)
        cv2.imshow('frame', frame)
        s = ""
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
"""

UDP_IP = "0.0.0.0"
UDP_PORT = 8389

sock = socket.socket()
sock.bind((UDP_IP, UDP_PORT))
sock.listen(1)
(new_socket, address) = sock.accept()
s = ""
while True:
    data = new_socket.recv(46080 / 5)
    s += data
    if len(s) == (46080 * 20):
        frame = numpy.fromstring(s, dtype=numpy.uint8)
        frame = frame.reshape(480, 640, 3)
        cv2.imshow('frame', frame)
        s = ""
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
