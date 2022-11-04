list=[]
for i in range(1,31):
    list.append(i*i)
print()

print("original list:",list)
print()

l1=list[:1]
print(l1)
print()
l2=list[-5:]
print(l2)
print()
for Square in l2:
    l1.append(Square)

print("my required list:",l1)

