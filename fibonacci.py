n = int(input("enter the number: "))
a,b=0,1
if n<=0:
    print("incorrect number")
elif n==1:
    print(a)
else:
    print(a,b,end=" ")
    for i in range(2,n):
        a,b=b,a+b
        print(b,end=" ")

print()

n=int(input("enter number: "))
a,b=0,1
for i in range(1,n+1):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    

        


        
        

        
