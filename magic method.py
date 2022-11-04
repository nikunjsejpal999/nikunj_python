 class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("init called")
        
    def __str__(self):
        print("str called")
        return "[{0},{1}]".format(self.a,self.b)

    def __add__(self,obj):
        x=self.a+obj.a
        y=self.b+obj.b
        print("add called")
        return Point(x,y)
   
obj1=Point(100,200)
print(obj1)
obj2=Point(300,400)
print(obj2)
print("Addition:",obj1+obj2)


