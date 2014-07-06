#!/usr/bin/env python3
#-*-coding:utf-8-*-
from persistent import Persistent

class Unit(Persistent):
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
        self.name='无名英雄'
    def __str__(self):
        return '姓名：{0},级别：{1},生命值：{2}，攻击力：{3}，颜色：{4}'.format(self.name,self.level,self.hp,self.atk,self.color)

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

#class Ashe(Hero):
    #def __init__(self,color='blue'):
        #Hero.__init__(self,1,474,49,color)
        #self.name='艾希'
        #self.addhp=79
        #self.addatk=3
        #self.skill=['聚精会神','冰霜射击','万箭齐发','鹰击长空','魔法水晶箭']

#if __name__ == '__main__':
