#!/usr/bin/env python3
#-*-coding:utf-8-*-
list001=['张三','李四','王二','麻子','李二','李一']
def zhsort(lst):
    from pypinyin import  lazy_pinyin
    pinyin=[lazy_pinyin(lst[i]) for i in range(len(lst))]
    lst0=[(a,b) for (a,b) in zip(lst,pinyin)]
    lst1= sorted(lst0, key=lambda d:d[1])
#    print(lst1)
    return [x[0] for x in lst1]
print(zhsort(list001))


def zhsort(lst):
    from pypinyin import  lazy_pinyin
    return [x[0] for x in sorted([(a,b) for (a,b) in zip(lst,[lazy_pinyin(lst[i]) for i in range(len(lst))])], key=lambda d:d[1])]


#if __name__ == '__main__': #if run as script


















