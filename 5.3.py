# -*- coding: utf-8 -*-
"""
Fix For Scapy Changing Input Output In Pycharm
"""
import sys  # For standard I/O

i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
import scapy.layers.inet


sys.stdin, sys.stdout, sys.stderr = i, o, e


def main():
    my_packet = sniff(count=10)
    print my_packet.show()
    # print my_packet[scapy.layers.inet.TCP].show
    pass  # Add Your Code Here


if __name__ == '__main__':
    main()