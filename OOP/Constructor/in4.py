class Book:
    def __init__(self,page):
        self.page=page
    def __sub__(self, other):
        return Book(self.page-other.page)
    def __mul__(self, other):
        return Book(self.page*other.page)
    def __str__(self):
        return str(self.page)


b=Book(25)
c=Book(10)
d=Book(5)
print(b-c-d)
print(b*c*d)
