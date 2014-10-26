#!/usr/bin/env python3
#-*-coding:utf-8-*-

from random import *
i_list = []
while len(i_list) < 100:
    i = 1
    while True:#一次实验
        x = randint(1,6)
        if x == 6:
            print('times:' , i)
            break
        else:
            print(x)
            i += 1
    i_list.append(i)

print(i_list)
from statistics import *
print(mean(i_list))#平均值
print(median(i_list))#中位数，去掉最高最低...





#if __name__ == '__main__':
