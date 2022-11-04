#remove last object
l=[1,2,3,"khushali","kotadiya",True,2.2,1]
print(l)

l.pop()
print(l)

#list

l2=[2,33,222,14,25]
print(l2[-1])

#remove dublicate value

l=list(dict.fromkeys(l))
print(l)


#append and exend

l.append(125)
print(l)

l.extend("khushali")
print(l)

#get the largest number, smallest num and sum of all from a list

L3=[20,25,54,78,89,1,100]
print(max(L3))
print(min(L3))
print(sum(L3))


#Write a Python program to count the number of strings where the string length is
#2 or more and the first and last
#character are same from a given list of strings.

l5=["TechnologiesT","topst","bhargavb","nikunjn","khushalik",'nikunjn']
print(l5.count('nikunjn'))








