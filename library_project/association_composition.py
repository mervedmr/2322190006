class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

lib = Library()
b1 = Book("1984")
lib.add_book(b1)
print([b.title for b in lib.books])
