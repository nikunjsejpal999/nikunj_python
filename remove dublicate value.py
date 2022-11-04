#remove dublicate value

l=[1,2,3,"khushali","kotadiya",True,2.2,1]
print(l)

l=list(dict.fromkeys(l))
print(l)


h=[*set(l)]
print(h)
