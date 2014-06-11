#!/usr/bin/env python3
#-*-coding:utf-8-*-

#import sys
#from tkinter import *

file001 = open('test.txt','w')
file001.write('hello world1\n')
file001.write('hello world2\n')
file001.close()

file001 = open('test.txt')
filetext=file001.read()
print(filetext)
file001.close()


#if __name__ == '__main__': #if run as script


















