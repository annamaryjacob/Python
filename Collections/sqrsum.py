lst=list()
x=0
limit=int(input("Enter limit of list"))
for i in range(0,limit):
    val=int(input("Enter value"))
    lst.append(val)
for item in lst:
    if(item%2==0):
        x=(item**2)+x
    else:
        pass
print(lst)
print("Sum of even squares",x)