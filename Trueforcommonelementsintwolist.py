def abc(list1,list2):
    for x in list1:
        for y in list2:

             if x == y:
                 result = True
                 return result

    else:
        result = False
        return result

list1 = [1,2,3,4,5]

list2 = [6,7,8,'a','b','b']
print(abc(list1,list2))


