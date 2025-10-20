class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __repr__(self):
        return f"Book({self.pages} pages)"

b1 = Book(100)
b2 = Book(150)
print(b1 + b2)
