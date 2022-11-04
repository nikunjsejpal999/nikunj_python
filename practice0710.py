import random

data=open("data.txt","w+")
for i in range(10):
    data.write(str(random.randint(1,100))+",")
    
data.seek(0)
l=data.read().split(",")[:-1]
print("main list: ",l)

prime=open("prime.txt","w+")

for i in l:
    if int(i) % 2 != 0:
        for j in range(3,int(int(i)/2)+1):
            if int(i)%j ==0:
                break
        else:
            prime.write(i+",")
    

prime.seek(0)
l2=prime.read().split(",")[:-1]
print("prime content is: ",l2)
data.close()
prime.close()

        
