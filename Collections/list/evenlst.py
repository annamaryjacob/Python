lst=list()
even=list()
limit=int(input("Enter limit of list"))
for i in range(0,limit):
    val=int(input("Enter value"))
    lst.append(val)
    if(val%2==0):
        even.append(val)
    else:
        pass
print(lst)
for item in (even):
    print(item)

#for item in lst:
    # if(item%2==0):
    #     print(item)
    # else:
    #     pass
