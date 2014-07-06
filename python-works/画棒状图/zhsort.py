#!/usr/bin/env python3
#-*-coding:utf-8-*-

#import sys
#from tkinter import *

from pypinyin import pinyin , lazy_pinyin

list001=['张三','李四','王二','麻子','李二','李一']
pinyinlist001=[lazy_pinyin(list001[i]) for i in range(len(list001))]

pinyindict={a:b for (a,b) in zip(list001,pinyinlist001)}
list002= sorted(pinyindict.items(), key=lambda d:d[1],)


print(list002)

#排序后的键列表
xticklist=[]
for x in list002 :
    xticklist.append(x[0])

print(xticklist)








#if __name__ == '__main__': #if run as script


















