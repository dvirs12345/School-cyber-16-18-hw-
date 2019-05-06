# Dvir Sadon
import sys
import random

i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, UDP
from scapy.layers.inet import TCP, IP

sys.stdin, sys.stdout, sys.stderr = i, o, e


def main():
    my_packet = sniff(count=1, filter='tcp and tcp.flags.syn==1 and tcp.flags.ack==0')  # should add another filter
    port = my_packet[TCP][0].dport
    if my_packet:
        new_packet = IP(dst='0.0.0.0')/TCP(dport=port, seq=random.randint(0, 10000), flags='SA')
        got = sr1(new_packet, timeout=0.8)
        if got:
            my_packet = sniff(count=1, filter='tcp')  # should add another filter
            while my_packet:  # ##
                pass
if __name__ == '__main__':
    main()
