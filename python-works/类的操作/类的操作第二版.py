#!/usr/bin/env python3
#-*-coding:utf-8-*-

#import sys
#from tkinter import *

class Hero():
    def addlevel(self):
        self.level=self.level+1
        self.hp=self.hp+self.addhp

class Garen(Hero):
    def __init__(self):
        self.level=1
        self.hp=455
        self.addhp=96
        self.skill=['不屈','致命打击','勇气','审判','德玛西亚正义']

garen001=Garen()
for i in range(6):
    print('级别:',garen001.level,'生命值：' ,garen001.hp)
    garen001.addlevel()
print('盖伦的技能有：',"".join([x + '  ' for x in garen001.skill]))


#if __name__ == '__main__': #if run as script


















