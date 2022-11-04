import random

data3=open("data3.txt","w+")
for i in range(10):
    data3.write(str(random.randint(1,100))+",")

data3.seek(0)
l=data3.read().split(",")[:-1]
print("your data: ",l)
prime=open("prime.txt","w+")

for i in l:
    if int(i)%2!=0:
        for j in range (3,int(int(i)/2)+1,2):
            if int(i)%j==0:
                break
                
        else:
            prime.write(i+",")
  
prime.seek(0)
l2=prime.read().split(",")[:-1]    
print("your prime content is:",l2)
prime.close()
data3.close()
