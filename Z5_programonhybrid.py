class Shape:
    def shapecalled(self):
        print("shapecalled ")

    def getS(self,l,h,w):
        self.l=l
        self.h=h
        self.w=w

    def putS(self):
        print("length: ",self.l)
        print("height: ",self.h)
        print("width: ",self.w)

class Square(Shape):
    def squarecalled(self):
        print("squarecalled")
    def areaofsquare(self):
        print("area is: ",4*self.l)

class Rectangle(Shape):
    def rectanglecalled(self):
        print("rectanglecalled")
    def areaofrectangle(self):
        print("area is: ",2*self.l*self.w)

class Box(Square,Rectangle):
    def boxcalled(self):
        print("boxcalled")
    def areaofbox(self):
        print("area is: ",self.l*self.h*self.w)

b1=Box()
l=int(input("L="))
h=int(input("H="))
w=int(input("W="))

b1.shapecalled()
b1.getS(l,h,w)
b1.putS()

b1.squarecalled()
b1.areaofsquare()

b1.rectanglecalled()
b1.areaofrectangle()

b1.boxcalled()
b1.areaofbox()




























        
    
