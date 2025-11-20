class Book:
    def checkout(self):
        print("Kitap verildi")

class Magazine:
    def checkout(self):
        print("Magazin verildi")

def give(item):
    item.checkout()

give(Book())
give(Magazine())
