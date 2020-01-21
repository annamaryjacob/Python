lst=list()
odd=list()
limit=int(input("Enter limit of list"))
for i in range(0,limit):
    val=int(input("Enter value"))
    lst.append(val)
    if(val%2!=0):
        odd.append(val)
    else:
        pass
print(lst)
for item in (odd):
    print(item)