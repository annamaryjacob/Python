class Person():
    def setPerson(self,age,name):
        self.age=age
        self.name=name

    def __str__(self):
        return self.name+str(self.age)

ob=Person()
ob.setPerson(25,"name")

print(ob)

#When we give print(ob) we get '<__main__.Person object at 0x7f92fee45ba8>'. This is the method called 2string method in the parent class
#'Object' which is a parent class for every class we make. We overide this method in our child class (def __str__(self) so that when
#we print ob we get only 'name'