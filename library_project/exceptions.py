class LibraryError(Exception):
    pass

class BookNotFound(LibraryError):
    pass

class Library:
    def __init__(self):
        self.books = []

    def find_book(self, title):
        for book in self.books:
            if book == title:
                return book
        raise BookNotFound(f"{title} not found")

lib = Library()
try:
    lib.find_book("1984")
except BookNotFound as e:
    print("Error:", e)
