
def pattern(n):
    for i in range(1,n+1):
        print("*"*i)

def oddoreven(n):
    if n%2==0:
        print("even number: ")
    else:
        print("odd number: ")

def maxoftwo(a,b):
    if a>b:
        print(a,"is greater number: ")
    else:
        print(b,"is greater number: ")

def maxofthree(a,b,c):
    if a>b:
        if a>c: 
            print(a,"is greater number: ")
        else:
            print(c,"is greater number: ")
    elif b>c:
        print(b,"is greater number: ")
    else:
        print(c,"is greater number: ")

def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n,"is not prime number : ")
                break
        else:
            print(n,"is prime number: ")
    else:
        print(n,"is not prime number: ")

def fibonacci(n):   
    a,b=0,1
    if n<0:
        print("incorrect number")
    elif n==1:
        print(a)
    else:
        print(a, b, end=" ")
        for i in range(2, n):
            a,b=b,a+b
            print(b, end=" ")
        

while True:
    print("1.pattern")
    print("2.oddoreven")
    print("3.maxoftwo")
    print("4.maxofthree")
    print("5.prime")
    print("6.fibonacci")
    print("7.exit")

    choice=int(input("enter your choice: "))
    print()

    if choice==1:
        n=int(input("enter number: "))
        pattern(n)
        print()

    elif choice==2:
        n=int(input("enter number: "))
        oddoreven(n)
        print()

    elif choice==3:
        a=int(input("enter number: "))
        b=int(input("enter number: "))
        maxoftwo(a,b)
        print()

    elif choice==4:
        a=int(input("enter number: "))
        b=int(input("enter number: "))
        c=int(input("enter number: "))
        maxofthree(a,b,c)
        print()

    elif choice==5:
        a=int(input("enter number: "))
        prime(a)
        print()

    elif choice==6:
        a=int(input("enter number: "))
        fibonacci(a)
        print()

    else:
        print("invalid choice")
        

