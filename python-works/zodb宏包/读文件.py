#!/usr/bin/env python3
#-*-coding:utf-8-*-


from ZODB import  DB


if __name__ == '__main__':
   # storage=FileStorage.FileStorage('test.zodb')
    db=DB('test.fs')
    connection=db.open()
    root=connection.root()

    print(root)


    for key in sorted(root):
        print(root[key])


    import transaction
    transaction.commit()
    db.close()



