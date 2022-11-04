import random

list5=[]
for i in range(20):
    list5.append(random.randint(1,10))

print(list5)

l=[*set(list5)]
print("your unique list is: ",l)
