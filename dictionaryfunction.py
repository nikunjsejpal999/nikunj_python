d={1:"dharma", 2:"khushali", 3:"tejal", 4:"bhargav", 5:"nikunj"}

print(d)
print(d[2])
print("*"*30)

d1=(d.copy())
print(d1)
print("*"*30)

print(d.fromkeys("3"))
print("*"*30)

print(d.get(3))
print("*"*30)

print(d.keys())
print("*"*30)

print(d.pop(5))
print(d)
print("*"*30)

print(d.popitem())
print(d)
print("*"*30)

d1={10:"parth", 20:"raj"}
d.update(d1)
print(d)

