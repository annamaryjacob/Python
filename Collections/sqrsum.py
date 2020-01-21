lst=list()
x=0
limit=int(input("Enter limit of list"))
for i in range(0,limit):
    val=int(input("Enter value"))
    lst.append(val)
for item in lst:
    if(item%2==0):
        x=item+x
    else:
        pass
print(lst)
print("Sum of prime numbers = ",x)