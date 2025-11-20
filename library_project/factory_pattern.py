class Book:
    def __init__(self, title):
        self.title = title

class BookFactory:
    @staticmethod
    def create(title):
        return Book(title)

b = BookFactory.create("1984")
print(b.title)
