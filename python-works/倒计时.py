#!/usr/bin/env python3
#-*-coding:utf-8-*-

import subprocess
#from tkinter import *
import time
#a is duration b is frequency
def beep(a,b):
    subprocess.Popen('play --no-show-progress --null --channels 1 synth %s sine %f' % ( a, b),shell=True)

print('''
这是一个简单地倒计时程序，输入秒数之后，
到达会发出警报声。
''')

count = 0
a = input('请输入倒计时几秒钟:')
b = int(a)
while (count < b):
    ncount = b - count
    print(ncount)
    time.sleep(1)
    count += 1

for x in range(1,10):
    beep(1,500)
    time.sleep(2)



#if __name__ == '__main__': #if run as script


















