class Parent:
    def phonee(self):
        print("I have a nokia 1100")

class Child(Parent):
    def phone(self):
        print("i have a phone")

c=Child()

c.phone()
c.phonee()

p=Parent()
p.phonee()
#child can invoke both phonee and phone but parent can only invoke phonee
#the child inherits all properties of Parent if Child(Parent) is used
