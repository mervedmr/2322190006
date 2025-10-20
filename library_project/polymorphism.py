class Member:
    def borrow(self):
        raise NotImplementedError

class Student(Member):
    def borrow(self):
        return "Student can borrow up to 3 books."

class Teacher(Member):
    def borrow(self):
        return "Teacher can borrow up to 10 books."

def borrow_books(members):
    for m in members:
        print(m.borrow())

borrow_books([Student(), Teacher()])
