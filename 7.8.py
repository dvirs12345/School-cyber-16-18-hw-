# Dvir Sadon
import sys
i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, UDP
from scapy.layers.inet import TCP, IP, ICMP

sys.stdin, sys.stdout, sys.stderr = i, o, e


def tracerout1(url):
    """makes a tracerout request using rising TTLs"""
    ip_list = []
    req = IP(dst=url)/ICMP(type="echo-request")  # makes a ping request
    packet1 = sr1(req)  # sends the ping request
    ip = packet1.src  # saves the ip of the ip
    real_packet = IP(dst=url, ttl=1)/ICMP(type="echo-request")  # makes the first packet
    got = sr1(real_packet, timeout=0.8)  # sends it
    counter = 2
    if got:
        ip_list.append(got.src)
    while got.src != ip:  # sends the request with rising TTL
        real_packet[IP].ttl = counter
        got = sr1(real_packet, timeout=0.8)
        if got:
            ip_list.append(got.src)
        counter += 1
    #  ip_list.append(ip)
    print ip_list


def main():
    """
    Add Documentation here
    """
    tracerout1("www.google.com")


if __name__ == '__main__':
    main()