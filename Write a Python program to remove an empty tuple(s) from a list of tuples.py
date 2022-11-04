tup = [(),('bhargav','15','8'),(),('tejal','nisha'),('krishna','akbar','45'),('dharma'),()]
print("main tuple:",tup)

print()
print()
for i in tup:
    if i==():
        tup.remove(i)
        
print("after remove empty tuple: ",tup)
