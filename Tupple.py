t=(1,2,1.1,2.2,True,"tops",[10,20,30],False,10,11,"python")

print(t)
print(t.count(1))
print(t.index(10))

for i in t:
    print(i)
    
print(t[6])

t[6].append(40)
print(t)
