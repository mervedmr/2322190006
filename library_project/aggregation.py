class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

b = Book("1984")
lib = Library()
lib.add_book(b)
print(lib.books[0].title)
