#!/usr/bin/env python3
#-*-coding:utf-8-*-

def isprime(n):
    #预置前面一点点会加快速度
    if n ==2:
        return True
    #按位与1，前面一定都是0个位数如果是1则
    #是奇数则返回1则真则假，如果是偶数则返回
    #0则假则真
    elif n<2 or not n & 1:
        return False
    #埃拉托斯特尼筛法...
#查一个正整数N是否为素数，最简单的方法就是试除法，将该数N用小于等于N**0.5的所有素数去试除，若均无法整除，则N为素数
    for x in range(3,int(n**0.5)+1,2):
        if n % x == 0:
            return False
    return True


def prime_next(lst):
    lstcopy=lst.copy()
    prime_next = lst[-1] +2
    while True:
        for i in lstcopy:
            if prime_next % i ==0:
                prime_next +=2
                continue
        lstcopy.append(prime_next)
        return lstcopy


def prime2(n):
    for x in range(n):
        if isprime(x):
            yield x

def prime(n):
    i=0
    x=1
    while i<n:
        if isprime(x):
            i +=1
            yield x
        x +=1

def prime_count(n):
    count = 0
    for i in range(2,n+1):
        if isprime(i):
            count += 1
    return count


def timeit(exp):
    import time
    start=time.clock()
    exec(exp)
    elapsed = (time.clock() - start)
    return elapsed

#if __name__ == '__main__':
    #pyout = open('素数.txt','w')
    #print(prime_next([2,3,5]))
    #print(isprime(10022221))
    #print(prime_count(100000))
    #print(timeit("prime_count(500000)"))
    #print([i for i in prime(500000)],file=pyout)
    #pyout.close()

#8.08       1baiwan

