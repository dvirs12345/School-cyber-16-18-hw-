# Dvir Sadon
import sys
i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, UDP
from scapy.layers.inet import TCP, IP, ICMP

sys.stdin, sys.stdout, sys.stderr = i, o, e


def make_packet():
    """makes and sends as the user wishes"""
    url = sys.argv[1]  # gets the url
    packets = sys.argv[2]  # gets the number of packets
    packets = int(packets)
    listi = []
    count = 0
    for times in range(packets):  # makes and sends packets
        req = IP(dst=url)/ICMP(type="echo-request", id=times)
        send(req)
    for times2 in range(packets):  # sniffs to get the packets sent
        listi.append(sniff(count=1))
        print listi[count]
        count += 1
    print "got: "+str(count)+" answers"


def main():
    make_packet()


if __name__ == '__main__':
    main()