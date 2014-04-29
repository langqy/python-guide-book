#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys
#from tkinter import *

a=input('请输入数值a：')
b=input('请输入数值b：')
c=input('请输入数值c：')
x1=input('请输入x轴最小值：')
x2=input('请输入x轴最大值：')
step=input('请输入step值：')
a=float(a);b=float(b);c=float(c);x1=float(x1);x2=float(x2);step=float(step)

pyout=open(sys.argv[1] ,"w")

while x1<x2:
    print(x1,a*x1**2+b*x1+c,file=pyout)
    x1=x1+step

pyout.close()

#if __name__ == '__main__': #if run as script



















