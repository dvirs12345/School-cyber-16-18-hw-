def deja():
    import re
    num = raw_input('-->')
    while int (num) > 100000 or re.search('[a-zA-Z]', num):
        print "enter for real this time d:)"
        num = raw_input()
    print num
    dat = num.split()
    print dat
    r = 0
    r = sum(map(int, str(num)))
    #while num:
    #    r,num = r+int(num)%10,int(num)//10
    print r
deja()