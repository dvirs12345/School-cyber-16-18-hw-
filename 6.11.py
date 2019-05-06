#Dvir Sadon
import sys  # For standard I/O

i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, UDP
sys.stdin, sys.stdout, sys.stderr = i, o, e


def main():
    """
    Add Documentation here
    """
    # print DNS().show()
    dns_packet = DNS(qdcount=1)/DNSQR(qname='www.google.com')
    # print dns_packet.show()
    # print ls(UDP)
    # dns_packet = UDP(sport=24601, dport=53)/DNS(qdcount=1)/DNSQR(qname='www.google.com')
    dns_packet = IP(dst='8.8.4.4')/UDP(sport=24601, dport=53)/DNS(qdcount=1, rd=1)/DNSQR(qname='www.google.com')
    response_packet = sr1(dns_packet)
    print response_packet.show()
if __name__ == '__main__':
    main()