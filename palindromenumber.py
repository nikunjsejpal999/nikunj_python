n=int(input("Enter The Number: "))
a=n
print(a)
print(type(a))
m=str(a)
j=(m[::-1])
k=int(j)
print(k)
print(type(k))  #type is use for checking that both datatypes are same or not

if k==a:
    print("The NUmber Is Palindrome")
else:
    print("The Number is not palindrome")
