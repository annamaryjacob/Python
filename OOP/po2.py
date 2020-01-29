class Parent:
    def property(self):
        print("10lack rs, 2cr, 5kg gold")
    def mrg(self):
        print("mrg with JM")
class Child(Parent):
    def mrg(self):
        print("mrg with JK")

c=Child()
c.property()
c.mrg()

#this is method over riding
#the parent and child require the same method name and the child requires its own implementation method


