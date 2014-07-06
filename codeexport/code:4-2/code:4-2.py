
class A():
    def __init__(self,a):
        self.a=a

    @staticmethod
    def fun():
        print('fun')

    def fun2(self,what):
        print('fun',what)

class B():
    def __init__(self):
        self.d=5
    b=2
    def fun3(self):
        print('fun3')

class C(A,B):
    def __init__(self):
        super().__init__(3)
        super().fun()
        super().fun2('what')
        super().fun3()

c=C()
print(c.a,c.b)

