# Dvirs Sadon
import sys
i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, UDP
from scapy.layers.inet import TCP, IP

sys.stdin, sys.stdout, sys.stderr = i, o, e

SA = 18


def main():
    for port in range(120, 1024):  # runs on these ports <<
        print "checking " + str(port)
        my_packet = TCP(dport=port, seq=123, flags='S')  # makes a tcp packet
        second_packet = IP(dst='192.168.10.188')/my_packet  # adds an IP packet to the tcp one
        got = sr1(second_packet, timeout=0.8)  # sends the macket and saves the one we got
        if got:  # if not None
            if got[TCP].flags == SA:  # checks if the message got is a 'SYN+ACK'
                print got.show()
                print 'OPEN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'


if __name__ == '__main__':
    main()