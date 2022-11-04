l1=[]
l2=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
for a in l2:
    if a not in l1:
        l1.append(a)

print(l1)
        
l1=[]
l2=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

l1=[*set(l2)]
print(l1)
