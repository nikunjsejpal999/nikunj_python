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
    while n>b:
        print(b,end=" ")
        a,b=b,a+b
    print()

while True:
    print("1.pattern")
    print("2.oddoreven")
    print("3.maxoftwo")
    print("4.maxofthree")
    print("5.prime")
    print("6.fibonacci")
    print("7.exit")

    choice=int(input("enter your choice: "))

    if choice==1:
        n=int(input("enter number: "))
        pattern(n)

    elif choice==2:
        n=int(input("enter number: "))
        oddoreven(n)

    elif choice==3:
        a=int(input("enter number: "))
        b=int(input("enter number: "))
        maxoftwo(a,b)

    elif choice==4:
        a=int(input("enter number: "))
        b=int(input("enter number: "))
        c=int(input("enter number: "))
        maxofthree(a,b,c)

    elif choice==5:
        a=int(input("enter number: "))
        prime(a)

    elif choice==6:
        a=int(input("enter number: "))
        fibonacci(a)

    else:
        print("invalid choice")
        

