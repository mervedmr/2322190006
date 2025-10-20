class Book:
    def __init__(self, title, stock):
        self.title = title
        self.__stock = stock

    def borrow(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if self.__stock < amount:
            raise ValueError("Not enough stock")
        self.__stock -= amount
        return self.__stock

    @property
    def stock(self):
        return self.__stock

book = Book("1984", 3)
print(book.title)
print(book.stock)
book.borrow(1)
print(book.stock)
