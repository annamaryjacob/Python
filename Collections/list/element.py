lst=[10,20,30,40]
flg=0
element=int(input("Enter element for search"))
for item in lst:
    if(item==element):
        flg+=1
        break
    else:
        flg=0
if(flg==0):
    print("Element not found")
else:
    print("Element found")


