lst=[10,10,20,30,40]
d=set(lst)
print(d)

# to remove duplicates from the list convert the list into set

st1={10,20,30,40}
st2={50,60,4,45}
#st1.union(st2)
#OR
#un=st1|st2
print("union of 2 sets=",un)
#TO FIND UNION OF 2 SETS

com=st1.intersection(st2)
print(com)

dif=st1.difference(st2)
print(dif)
