print('hello world')


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def getName(self):
        return self.name
    def getAuthor(self):
        return self.author
    def setName(self, name):
        self.name = name
    def setAuthor(self, author):
        self.author = author


Book1 = Book("Book1", "Niladri")
print(Book1.getAuthor())
print(Book1.getName())
