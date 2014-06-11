#!/usr/bin/env python3
#-*-coding:utf-8-*-

#import sys
#from tkinter import *

class Hero():
    def addlevel(self):
        self.level=self.level+1
        self.hp=self.hp+self.addhp

class Garen(Hero):
    level=1
    hp=455
    addhp=96
    skill=['不屈','致命打击','勇气','审判','德玛西亚正义']

garen001=Garen()

for i in range(18):
    print('级别:',garen001.level,'生命值：' ,garen001.hp)
    garen001.addlevel()


#if __name__ == '__main__': #if run as script


















