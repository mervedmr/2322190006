class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __repr__(self):
        return f"Book({self.title!r})"

b = Book("1984", 300)
print(len(b))
print(b)
