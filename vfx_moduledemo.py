import vfx

while True:
    print('1. pattern')
    print('2. oddeven')
    print('3. maxoftwo')
    print('4. maxofthree')
    print('5. fibonacci')
    print('6. prime')

    choice=int(input('enter your chice : '))

    if choice==1:
        a=int(input("enter value : "))
        vfx.pattern(a)
    elif choice==2:
        a=int(input("enter  value : "))
        vfx.oddeven(a)
    elif choice==3:
        a=int(input("enter value :"))
        b=int(input("enter value :"))
        vfx.maxoftwo(a,b)
    elif choice==4:
        a=int(input("enter value: "))
        b=int(input("enter value: "))
        c=int(input("enter value: "))
        vfx.maxofthree(a,b,c)
    elif choice==5:
        a=int(input("enter value: "))
        vfx.fibonacci(a)
    elif choice==6:
        a=int(input("enter value: "))
        vfx.prime(a)
    else:
        break
