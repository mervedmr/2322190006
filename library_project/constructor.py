class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Created book: {self.title} by {self.author}")

    def describe(self):
        print(f"'{self.title}' written by {self.author}")

book = Book("1984", "George Orwell")
book.describe()
