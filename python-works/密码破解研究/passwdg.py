#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys
from random import *
#from tkinter import *
numlst=[0,1,2,3,4,5,6,7,8,9]
salst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
balst=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#这里有很大的优化空间
j=1

trytimes=100000#密码个数
SystemRandom()

while j <= trytimes:
    i=1
    k=1
    lst=''
    numc=randrange(1,9)#密码位数#这里有很大的优化空间
    sac=randrange(1,9)
    while i <=sac:
        lst=lst+str(choice(salst))
        i=i+1
    while k <=numc:
        lst=lst+str(choice(numlst))
        k=k+1

    print(lst)
    j=j+1




#if __name__ == '__main__': #if run as script


















