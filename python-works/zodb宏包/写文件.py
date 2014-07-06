#!/usr/bin/env python3
#-*-coding:utf-8-*-

from ZODB import DB
from Hero import Garen

#1.先creat FileStorage  再DB
#2.直接DB
#3.DB(None)  临时操作文件

if __name__ == '__main__':
   # storage=FileStorage.FileStorage('test.zodb')
    db=DB('test.fs')
    connection=db.open()
    root=connection.root()
    garen1=Garen()
    garen2=Garen('red')
    garen3=Garen('yellow')
    for (key,item) in [('garen1',garen1),('garen2',garen2),('garen3',garen3)]:
        root[key]=item


    import transaction
    transaction.commit()
#transaction.abort() 或者取消所有更改
    db.close()

