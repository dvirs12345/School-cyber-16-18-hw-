# Itay Twizer and Dvir Saadon
import sys

i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *

sys.stdin, sys.stdout, sys.stderr = i, o, e


def main():
    port_word = ''
    packets = sniff(count=1, filter='udp and portrange 24023-24126')
    # ^sniffing by the udp protocol filter and the port range: 24023-24126
    port_word += chr((packets[UDP][0].dport) - 24000)
    # ^creates the message - subtracting the port by 24000 and turning it to a character
    while packets[IP][0].ttl:
        # ^keeps running while the last packet's time to live is not 0
        packets = sniff(count=1, filter='udp and portrange 24023-24126')
        # ^sniffing by the udp protocol filter and the port range: 24023-24126
        port_word += chr((packets[UDP][0].dport) - 24000)
        # ^creates the message - subtracting the port by 24000 and turning it to a character
    print 'The secret message:' + port_word[:len(port_word) - 1]
    # ^prints the message


if __name__ == '__main__':
    main()
