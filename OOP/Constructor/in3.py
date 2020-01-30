
#To add the pages of 2 books and display the sum
# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __add__(self, other):
#         return (self.pages+other.pages)
#
#     def __str__(self):
#         return self.pages
#
# b=Book(200)
# b1=Book(100)
# print(b+b1)


#To add the pages of more than 2 books and display the sum
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return str(self.pages)

b=Book(200)
b1=Book(100)
b2=Book(300)

print(b+b1+b2)