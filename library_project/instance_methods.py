class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Merhaba ben", self.name)

u = User("Merve")
u.greet()
