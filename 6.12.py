#Dvir Sadon
import sys  # For standard I/O

i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, UDP,DNSRR
sys.stdin, sys.stdout, sys.stderr = i, o, e


def main():
    """
    Add Documentation here
    """
    dest = raw_input("enter the site:")
    dns_packet = IP(dst='8.8.4.4')/UDP(sport=24601, dport=53)/DNS(qdcount=1, rd=1)/DNSQR(qname=dest)
    response_packet = sr1(dns_packet)
    print response_packet[DNSRR][1].rdata
if __name__ == '__main__':
    main()