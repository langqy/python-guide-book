
class Hero():
    def addlevel(self):
        self.level=self.level+1
        self.hp=self.hp+self.addhp

class Garen(Hero):
    level=1
    hp=455
    addhp=96

garen001=Garen()
for i in range(6):
    print('级别:',garen001.level,'生命值：' ,garen001.hp)
    garen001.addlevel()

