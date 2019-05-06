# -*- coding: utf-8 -*-
PI = 3.14
class zura(object):
    def __init__(self, color):
        self.color = color

    def setcolor(self, color):
        self.color = color
    def getcolor(self):
        return self.color
    def getshetch(self):
        pass
    def gethekef(self):
        pass
class malben(zura):
    def __init__(self, color, orech, rochav):
        self.color = color
        self.orech = orech
        self.rochav = rochav

    def getarea(self):
        return self.rochav*self.orech

    def gethekef(self):
        return self.rochav*2+self.orech*2

class circle(zura):
    def __init__(self, color, R):
        self.color = color
        self.R = R

    def getarea(self):
        return self.R*self.R*PI

    def gethekef(self):
        return self.R*PI*2

class square(zura):
    def __init__(self, color, zela):
        self.color = color
        self.zela = zela

    def getarea(self):
        return self.zela*self.zela

    def gethekef(self):
        return self.zela*4

def main():
    pass


