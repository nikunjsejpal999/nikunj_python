mainlist=[5,6,3,8,2,1,7,1]
print("length of mainlist :",len(mainlist))

sublist=[8,2,1]
print("length of sublist :",len(sublist))

result=False

for i in (mainlist):
    if mainlist[i:i+len(sublist)] == sublist:
            result = True
            break
		
print("Is sublist present in list ?:",result)
