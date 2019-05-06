# Dvir Sadon
import sys
import random

i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, UDP
from scapy.layers.inet import TCP, IP

sys.stdin, sys.stdout, sys.stderr = i, o, e


IPE = '10.0.0.20'


def ThreeWayHandshake(dport):
    my_packet = TCP(dport=dport, seq=random.randint(0, 10000), flags='S')
    second_packet = IP(dst=IPE) / my_packet
    got = sr1(second_packet, timeout=0.8)
    if got:
        Apcket = IP(dst=IPE) / TCP(dport=dport, seq=got.ack + 1, ack=got.seq + 1, flags='A')
        send(Apcket)


def dividestring(nek):
    randnum = random.randint(0, len(nek))  # the number to add
    divided = []
    while nek != '':
        divided.append(nek[0:randnum])
        nek = nek[randnum:]
        randnum = random.randint(0, len(nek))  # the number to add
    print divided
    return divided


def make_a_list(list2, sequ):
    packetlist = []
    for place in list2:
        deport = random.randint(1000, 65535)
        wat = IP(dst=IPE) / TCP(dport=deport, seq=sequ)
        print sequ
        sequ += len(place)
        packetlist.append(wat)
    random.shuffle(packetlist)
    # packet_help = packetlist[:len(packetlist)-1]
    for place2 in packetlist:
        ThreeWayHandshake(place2[TCP].dport)
        send(place2)
    return packetlist


def main():
    # print dividestring(raw_input('--enter a string'))
    # ThreeWayHandshake(12345)
    make_a_list(dividestring(raw_input('--enter a string: ')), 123)


if __name__ == '__main__':
    main()
