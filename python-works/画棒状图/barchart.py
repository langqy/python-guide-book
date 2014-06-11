#!/usr/bin/env python3
#-*-coding:utf-8-*-

#created by wanze
#feel free
#version 0.2

#import sys
#from tkinter import *


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
from pypinyin import pinyin , lazy_pinyin#汉字转拼音
#用于排序


zhfont1 = matplotlib.font_manager.FontProperties(fname='/home/wanze/.fonts/msyh.ttf')

def randrgb():
    '''Generate a random rgb color.'''
    return (random.random(), random.random(), random.random())



import xlrd#read xls
#import xlwt#write xls
workbook =xlrd.open_workbook('test.xls')
sheet1=workbook.sheet_by_index(0)

#print(sheet1.nrows,sheet1.ncols)

dict001={sheet1.cell_value(r,0):sheet1.cell_value(r,1) for r in range(sheet1.nrows)}

list001=list(dict001.keys())
pinyinkeys=[lazy_pinyin(list001[i]) for i in range(len(list001))]

pinyindict={a:b for (a,b) in zip(list001,pinyinkeys)}
list002= sorted(pinyindict.items(), key=lambda d:d[1],)

#排序后的键列表
xticklist=[]
for x in list002 :
    xticklist.append(x[0])
valuelist=[]
for key in xticklist:
    valuelist.append(dict001.get(key))

barlist=plt.bar(range(len(dict001)), valuelist,align="center")

for x in range(0,9):
    barlist[x].set_color(randrgb())

plt.xticks(range(len(dict001)),xticklist,fontproperties=zhfont1)

def autolabel(rects):
# attach some text labels
    for ii,rect in enumerate(rects):
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%s'% (valuelist[ii]),
                ha='center', va='bottom')
autolabel(barlist)

plt.axis([-1,10]+[1,12000])
plt.show()

#if __name__ == '__main__': #if run as script


















