
class A:
    def show(self):
        print("show from A")

class B(A):
    def show(self):
        super().show()
        print("show from B")

class C(B):
    def show(self):
        super().show()
        print("show from C")

c1=C()
c1.show()


print("*"*50)
print("*"*50)
print("*"*50)
''' 
#for multiple inheritance
class A:
    def showA(self,a):
        self.a=a
    def putA(self):
        print("show from A:",self.a)

class B:
    def getB(self,b):
        self.b=b
    def putB(self):
        print("show from B:",self.b)
        

class C(A,B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("show from C:",self.c)
c1=C()
c1.getA(10)
c1.getB(20)
c1.getC(30)
c1.putA()
c1.putB()
c1.putC()
'''
