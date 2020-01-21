lst=[1,2,3,4,5,6,7,8,9,10]
add=list()
val=int(input("Enter value"))
length=len(lst)
for i in lst:
    num=lst[i]-val
    for item in lst:
        if(num==item):
            add.append (num)
        else:
            break
    break





