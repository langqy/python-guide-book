#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys
#from tkinter import *
string001 =''
while True :
    x=input('请输入文字：')
    string001= string001+x
    if x=='quit':
        break

pyout=open(sys.argv[1] ,"w")
print(string001 , file=pyout)


pyout.close()


#if __name__ == '__main__': #if run as script



















