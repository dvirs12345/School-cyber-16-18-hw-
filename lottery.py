# -*- coding: utf-8 -*-
import re
import random
def func1():
    help_list = []
    for num in range(6):
        help_list[num] = random.randint(1, 37)
    help_list.append(random.randint(1, 7))
    help_list.sort()
    first_arr = []
    while got != 'stop':
        got = raw_input("enter the numbers: ")
        first_arr = re.findall(r"[\w']+", got)
        if first_arr in help_list:
            print 'you won the first prize'








def main():
    """
    Add Documentation here
    """
    pass  # Add Your Code Here
