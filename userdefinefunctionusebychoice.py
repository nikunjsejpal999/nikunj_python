def pattern(n):
    for i in range(1,n+1):
        print("*"*i)
#i=int(input("enter n: "))


def oddeven(n):
    if n%2==0:
        print("N is even number")
    else:
        print("N is odd number")
        
#i=int(input("enter a: "))

#oddeven(i)

def maxoftwo(a,b):
    if a>b:
        print("A is greater number: ")
    else:
        print("B is greater number: ")

#x=int(input("enter C: "))
#y=int(input("enter D: "))

#maxoftwo(x,y)

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print("A is greater number ")
        else:
            print("C is greater number ")
    elif b>c:
            print("B is greater number ")
    else:
            print("C is greater number ")

#p=int(input("enter E: "))
#q=int(input("enter F: "))
#r=int(input("enter G: "))

#maxofthree(p,q,r)


#whenever use choice function "true" is important function.
            
while True:
      print("1: pattern")
      print("2: oddeven")
      print("3: maxoftwo")
      print("4: maxofthree")
      c=int(input("enter choice"))

      if c==1:
        n=int(input("enter number:"))
        pattern(n)
      elif c==2:
          a=int(input("enter number:"))
          oddeven(a)
      elif c==3:
          b=int(input("enter number:"))
          c=int(input("enter number:"))
          maxoftwo(b,c)
      elif c==4:
          d=int(input("enter number:"))
          e=int(input("enter number:"))
          f=int(input("enter number:"))
          maxofthree(d,e,f)
      else:
          print("exit")
          break


