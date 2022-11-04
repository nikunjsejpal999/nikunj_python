l=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6]

#method-1
print(l)
print()
l = list(dict.fromkeys(l))
print(l)
print()

#method-2

res=[*set(l)]
print(res)

#method-3

res1=[]
[res1.append(x) for x in l if x not in res1]
print("res1:",res1)
