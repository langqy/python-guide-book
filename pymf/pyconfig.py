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

def dosomething(n):
    if n==0:
        pass
    elif n==1:
        print('do!')
    else:
        print('do!')
        return dosomething(n-1)

def subst(list001,element001,element002):
    try:
        list001.index(element001)
    except ValueError:
        return list001
    else:
        n=list001.index(element001)
        del list001[n]
        list001[n:n]=[element002]
        return subst(list001,element001,element002)


############我定义的类##############


if __name__ == '__main__': #if run as script
    dosomething(10)



















