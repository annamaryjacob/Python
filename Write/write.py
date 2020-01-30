# lst=["Anna","Mary","Jacob",9,6,99]
# f=open("Writedemo.txt","w")
# for item in lst:
#     f.write(str(item))
#     f.write("\n")

num=[1,2,3,4,5,6,7,8,9,10]


f=open("even.txt","w")
f2=open("Odd.txt","w")
for numb in num:
    if numb%2==0:
        f.write(str(numb))
        f.write("\n")
    else:
        f2.write(str(numb))
        f2.write("\n")
