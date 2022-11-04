l=[1,2,1.1,2.2,"tops",True,10,"python",False,1,2]

print(l)
l.append(100)
print(l)

#l.clear()
#print(l)

l1=l.copy()
print(l1)

print(l.count(2))


l2=[101,102,103]
l.extend(l2)
print(l)

print(l.index(10))

l.insert(5,1000)
print(l)

l.pop()
print(l)

l.pop(10)
print(l)

l.remove(10)
print(l)

l5=[1,2,3,4,5,6,1,1,1]
l5.remove(1)
print(l5)
