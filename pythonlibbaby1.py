# -*- coding: utf-8 -*-
def main():
    """
    Add Documentation here
    """

    for things in range(1,41):#q1
       print things


    couter = 0;#q2
    while couter!=40:
        couter = couter+1
        print couter

    for x in range(0,51):
        if x%10 ==0:
            print(x/10)
        else:
             print x*0.1

    for x in range(0,101):
        if x%7 == 0:
            print x
        elif x%10==7 or x/10%10==7:
            print x

    pass  # Add Your Code Here
if __name__ == '__main__':
    main()