# Dvir Sadon and Itay Twizer
import time
import sys

i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, UDP

sys.stdin, sys.stdout, sys.stderr = i, o, e


def main():
    message = raw_input('Enter the message:')
    my_list = list(message)  # makes the message into a list of chars
    for letters in my_list:  # scans the list
        # makes the main packet
        dns_packet = IP(dst='192.168.10.76') / UDP(sport=24601, dport=24000 + ord(letters)) / ''
        port = dns_packet[UDP].dport  # gets the destenation port of the packet given
        send(dns_packet)  # Sends the packet to the server
        time.sleep(0.09)  # A delay so the packet will send without losing parts
        # makes a packet with the ttl 0 so that the server will know when to stop sniffing.
    end_packet = IP(dst='192.168.10.76', ttl=0)/UDP(sport=24601, dport=24100)
    send(end_packet)  # sends the packet that says its the last one

main()
# 32-126