#!/usr/bin/env python3
#-*-coding:utf-8-*-

#import sys

class Unit():
    def __init__(self,hp,atk,color):
        self.hp=hp
        self.atk=atk
        self.color=color
    def __str__(self):
        return '生命值：{0}，攻击力：{1}，颜色：{2}'.format(self.hp,self.atk,self.color)

class Hero(Unit):
    def __init__(self,level,hp,atk,color):
        Unit.__init__(self,hp,atk,color)
        self.level=level
    def __str__(self):
        return '级别：{0},生命值：{1}，攻击力：{2}，颜色：{3}'.format(self.level,self.hp,self.atk,self.color)

    def addlevel(self):
        self.level=self.level+1
        self.hp=self.hp+self.addhp
        self.atk=self.atk+self.addatk

class Garen(Hero):
    def __init__(self,color='blue'):
        Hero.__init__(self,1,455,56,color)
        self.name='盖伦'
        self.addhp=96
        self.addatk=3.5
        self.skill=['不屈','致命打击','勇气','审判','德玛西亚正义']

if __name__ == '__main__':
    garen001=Garen('red')
    garen002=Garen()
    print(garen001)
    unit001=Unit(1000,1000,'gray')
    print(unit001)
    for i in range(6):
        print(garen001)
        garen001.addlevel()
    print('盖伦的技能有：',"".join([x + '  ' for x in garen001.skill]))



















