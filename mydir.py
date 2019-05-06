# -*- coding: utf-8 -*-
import os
import time
import win32file


def freespace(p):
    """
    Returns the number of free bytes on the drive that p is on
    """
    secsPerClus, bytesPerSec, nFreeClus, totClus = win32file.GetDiskFreeSpace(p)
    return secsPerClus * bytesPerSec * nFreeClus


arr = os.listdir("./")
arr2 = []  # array for the dir and shit
counter = 0
numofdirs = 0
arr3 = []
arr4 = []
dircount = 0
filecount = 0
sumsize = 0
for sss in arr:
    arr4.append(time.ctime(os.stat(sss).st_mtime))
    if os.path.isdir(sss):
        arr2.append("<DIR>")
        arr3.append('')
        numofdirs += 1
        dircount += 1
    else:
        arr2.append("     ")
        arr3.append(os.path.getsize(sss))
        sumsize += os.path.getsize(sss)
        filecount += 1
    counter += 1

for shh in range(len(arr)):
    if arr2[shh] is not '<DIR>':
        print '{:25} {:^5} {:^6} {}'.format(arr4[shh], arr2[shh], str(arr3[shh]), arr[shh])
    else:
        print '{:25} {:5} {:>16}'.format(arr4[shh], arr2[shh], arr[shh])

print str(filecount) + ' File(s)        ' + str(sumsize) + ' bytes'
print str(dircount) + ' Dir(s)          ' + str(freespace('./')) + ' bytes free'

# print arr4
# print arr
# print arr3
# print time.ctime(os.stat("F:/wallpapers/img15.jpg").st_mtime)
# print arr2
