lst=[3,9,8,4,5,7,6,2]
lst.sort()
print(lst)
flg=1
val=int(input("Enter search value"))
length=len(lst)
lower=0
upper=length
mid=(lower+upper)//2
while(lower<upper):
    if(val<lst[mid]):
        upper=mid-1
    elif(val>lst[mid]):
        lower=mid+1
    elif(val==lst[mid]):
        flg=0
        break
    mid=(lower+upper)//2
if(flg==0):
    print("Element found")
else:
    print("Element not found")



