
#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import *


mainwindow=Tk()

def quit(event):
    print('拜拜......')
    sys.exit()

def hello(event):
    print('双击')

def greeting(event):
    print('你好')


Label(text='你好').pack( side=TOP)


button001=Button(mainwindow, text='点我')
button001.pack(side=LEFT)


button001.bind('<Button-1>',hello)
button001.bind('<Double-1>',quit)#多个事件

button002=Button(mainwindow, text='你好')
button002.pack(side=RIGHT)
button002.bind('<Button-1>',greeting)

mainloop()

