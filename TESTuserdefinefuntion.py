def test(a=40,b=30,c=20,d=10):
        print("A: ",a, "B: ",b, "C: ",c, "D: ",d)

test(1,2,3,4)
test(1,2,3)
test(1,2)
test(1)
test()
test(b=100,d=200)
print()

def test(a,b,c,d):
    print("A:",a, ",B:",b, ",C:",c, ",D:",d)
test(1,2,3,4)
print()



def test(a,b,c,*d):
    print("A:",a, ",B:",b, ",C:",c, ",it's become a tuple D:",d)
test(1,2,3,4,5,6,7,8,9)
print()


def test(a,b,c,*d):
    print("A:",a, ",B:",b, ",C:",c, ",it's become a list D:",list(d))
test(1,2,3,4,5,6,7,8,9)
print()


def test(a,b,c,*d,**e):
    print("A:",a, ",B:",b, ",C:",c, ",it's become a tuple D:",d, ",it's become a dictionary E:",e)
test(1,2,3,4,5,6,7,8,9,x=10,y=20,z=30)
print()
