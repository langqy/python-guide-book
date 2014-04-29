#!/usr/bin/env python3
#-*-coding:utf-8-*-

#import sys
#from tkinter import *

while True:
    x=input('请输入一个数值，我将返回它除以2之后的数值\n输入"quit"退出\n')
    if x=='quit':
        break
    try :
        num=float(x)
    except:
        print('输入有错')
    else:
        print(num/2)
print('再见')

#if __name__ == '__main__': #if run as script


















