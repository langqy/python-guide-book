#!/usr/bin/env python3
#-*-coding:utf-8-*-

import shelve
from Hero import Garen

if __name__ == '__main__':
    garen1=Garen()
    garen2=Garen('red')
    garen3=Garen('yellow')
    db=shelve.open('test.db')
    for (key,item) in [('garen1',garen1),('garen2',garen2),('garen3',garen3)]:
        db[key]=item
    db.close()

