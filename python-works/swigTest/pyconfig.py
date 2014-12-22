#!/usr/bin/env python3
#-*-coding:utf-8-*-

# 我的python3环境的基本配置
##################################
#序言部分
import sys
#from PyQt4  import Qt
#from PyQt4  import QtGui
#from PyQt4  import QtCore
#from tkinter import *
import math

#########我定义的函数###############
#菲波那奇数列
def fib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)




############我定义的类##############


if __name__ == '__main__': #if run as script
    dosomething(10)



















