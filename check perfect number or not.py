n=int(input("Enter The Number:- "))

s=0
for i in range(1,(n//2)+1):
   if n%i==0:
       s=s+i
if n==s:
    print("The number is perfect")
else:
    print("The number is not perfect")
