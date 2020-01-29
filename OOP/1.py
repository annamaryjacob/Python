class Person:
    def setPerson(self,age,name):
        self.age=age
        self.name=name

    def printPerson(self):
        print("name=",self.name)
        print("age=",self.age)

class Student(Person):         #student is a person ('is a' relationship)

    def setStudent(self,rol,course):
        self.rol=rol
        self.course=course
    def printDetails(self):
        print("rol=",self.rol)
        print("course=",self.course)

ob=Student()
ob.setPerson(20,"Anna")
ob.setStudent(4,"bcom")
ob.printPerson()
ob.printDetails()

