go=[2,3,4,5,"6",7,8,9.8,10]
#lists can hold different types of data
#to update use following syntax
go[2]=4.6
go.append(11)
go.insert(6,7.5)
print(go)

#print the list one by one
# st=[10,20,30,40]
# cnt=len(st)
# print(cnt)
# for i in range(0,cnt):
#     print(st[i])


for item in go:
    print(item)

#to print only even numbers in the list
op=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
cnt=len(op)

for i in range(0,cnt):
    if(op[i]%2==0):
        print(op[i])
    else:
        pass


