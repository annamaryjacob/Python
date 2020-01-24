lst=list()
limit=int(input("Enter limit of list"))
for i in range(0,limit):
    val=int(input("Enter value"))

    lst.append(val)  #lst[i]=val instead of append function

print(lst)