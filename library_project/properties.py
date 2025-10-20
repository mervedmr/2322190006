class Book:
    def __init__(self, title, pages):
        self.title = title
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value < 1:
            raise ValueError("Book must have pages")
        self._pages = value

b = Book("1984", 328)
print(b.pages)
b.pages = 300
print(b.pages)
