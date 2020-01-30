#To print the names of the people whose salary is more than 20000 and also print the count of people whose salary exceeds 25000
class Person:
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal

    def __str__(self):
        return self.name
f=open("/home/anna/Python/OOP/Person","r")
lst=[]
twf=[]
for data in f:
    persons=data.rstrip("\n").split(",")
    age=persons[0]
    name=persons[1]
    sal=persons[2]
    if int(sal)>=20000:
        ob=Person(age,name,sal)
        lst.append(ob)
    else:
        pass
    if int(sal)>25000:
        twf.append(sal)
    else:
        pass
for item in lst:
    print(item)
print(twf)
x=len(twf)
print("The number of people with salary more than 25000 is",x)