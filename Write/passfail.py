


f=open("/home/anna/Python/Write/Student","r")
f1=open("/home/anna/Python/Write/pass","r")
f2=open("/home/anna/Python/Write/fail","w")

# for item in f:
#     if item not in f1:
#         f2.write(str(item))

s1=set()
ps=set()

for a in f:
    s1.add(a.rstrip("\n"))
for b in f1:
    ps.add(b.rstrip("\n"))
s3=s1.difference(ps)
print(s3)
for i in s3:
    f2.write(str(i,))
    f2.write("\n")

