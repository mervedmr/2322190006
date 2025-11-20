from typing import Protocol

class Checkable(Protocol):
    def checkout(self, user): ...

class Book:
    def checkout(self, user):
        print(f"{user} kitabı aldı")

def process(item: Checkable, user):
    item.checkout(user)

process(Book(), "Merve")
