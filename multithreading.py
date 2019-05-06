# -*- coding: utf-8 -*-
import threading
import urllib


#def getall():
#    for shh in xrange(1, 32):
#        name = urllib.urlopen('http://cyber.org.il/os/demo/movie'+str(shh)+'.txt')
#        for i in name:
#            print i
#        print ""
def getone(wut):
    name = urllib.urlopen('http://cyber.org.il/os/demo/movie'+str(wut)+'.txt')
    for i in name:
        print i


def getall():
    for shh in xrange(1, 32):
        t = threading.Thread(target=getone, args={shh})
        t.start()

#  t = threading.Thread(target=thread_func, args=(1, 2))
#  t.start()
#  t.join()

getall()