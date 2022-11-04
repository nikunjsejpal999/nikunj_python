a=int(input("Enter First Number:-"))
b=int(input("Enter Second Number:-"))
small=0
if a<b:
    small=a
else:
    small=b

for i in range(small,0,-1):
    if a%i==0 and b%i==0:
        print("HCF is:-",i)
        break
