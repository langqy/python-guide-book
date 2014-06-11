#!/usr/bin/env python3
#-*-coding:utf-8-*-

#import sys
#from tkinter import *

with open('test.txt','w') as file001:
    file001.write('hello world1\n')
    file001.write('hello world2\n')


with open('test.txt','r') as file001:
    filetext=file001.read()
    print(filetext)


#if __name__ == '__main__': #if run as script


















