#!/usr/bin/env python3
#-*-coding:utf-8-*-

#import sys
#from tkinter import *
import random

print('''
这个程序定义了两个函数：
randrgb()  返回[0-1]的rgb值
randRGB() 返回 [0-255]的RGB值


''')

def randrgb():
    return (random.random(), random.random(), random.random())

def randRGB():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))



print(randrgb())
print(randRGB())











#if __name__ == '__main__': #if run as script


















