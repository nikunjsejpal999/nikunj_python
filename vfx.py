def pattern(n):
    for i in range(1,n+1):
        print("*"*i)
#i=int(input("enter n: "))


def oddeven(a):
    if a%2==0:
        print("A is even number")
    else:
        print("A is odd number")
        
#i=int(input("enter a: "))

#oddeven(i)

def maxoftwo(a,b):
    if a>b:
        print(a ," is greater number: ")
    else:
        print(b," is greater number: ")

#x=int(input("enter C: "))
#y=int(input("enter D: "))

#maxoftwo(x,y)

def maxofthree(e,f,g):
    if e>f:
        if e>g:
            print(e, "is greater number ")
        else:
            print(g, "is greater number ")
    elif f>g:
            print(f, "is greater number ")
    else:
            print(g, "is greater number ")
           

def fibonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=' ')
        a,b=b,a+b
    print()
        



def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n,'is not prime:')
                break
        else:
            print(n, " is prime")

    else:
        print(n,'is not  prime' )

        

