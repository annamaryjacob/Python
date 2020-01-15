m1=int(input("Enter the first mark"))
m2=int(input("Enter the second mark"))
m3=int(input("Enter the third mark"))
tot=m1+m2+m3
print(tot)
if(tot>=145):
    print("Your grade is A+")
elif(tot>=140):
    print("Your grade is A")
elif(tot>=135):
    print("Your grade is B+")
elif(tot>=130):
    print("Your grade is B")
else:
    print("You have failed")
