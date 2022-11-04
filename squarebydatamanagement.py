import random

data2=open("data2.txt","w")
for i in range (10):
    data2.write(str(random.randint(1,100))+",")
data2.close()

data2=open("data2.txt","r")
print(data2.read())
data2.seek(0)
square=open("square.txt","w")
cube=open("cube.txt","w")

l=data2.read().split(",")[:-1]
for i in l:
    sq=int(i)
    square.write(str(sq*sq)+",")
    print(sq*sq,end=",")
    cube.write(str(sq*sq*sq)+",")
    print(sq*sq*sq)
    print()

square.close()    
cube.close()
data2.close()
'''
print("data file content")
data2=open("data2.txt","r")
print(data2.read())
data2.close()

print("square file content")
square=open("square.txt","r")
print(square.read())
square.close()

print("cube file content")
cube=open("cube.txt","r")
print(cube.read())
cube.close()
'''

