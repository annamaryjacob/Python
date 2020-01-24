lst=[1,2,3,4,5,6,7,8,9,10]
lst.sort()
print(lst)
val=int(input("Enter value"))
length=len(lst)
low=0
upper=length-1
x=0
while(low<upper):
    res = lst[low] + lst[upper]
    if(val<res):
        upper=upper-1
    elif(val>res):
        lower=lower+1
    elif (val == res):
        print(lst[low], lst[upper])
        low=low+1








