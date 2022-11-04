import random

data=open("data.txt","w+")
for i in range(10):
    data.write(str(random.randint(1,100))+",")
    
data.seek(0)
l=data.read().split(",")[:-1]
print("main file data is: ",l)

odd=open("odd.txt","w+")
even=open("even.txt","w+")

for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
odd.seek(0)
even.seek(0)
l1=odd.read().split(",")[:-1]
print("odd number is: ",l1)
l2=even.read().split(",")[:-1]
print("even number is: ",l2)

data.close()
odd.close()
even.close()


