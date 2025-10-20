from abc import ABC, abstractmethod

class AbstractMember(ABC):
    @abstractmethod
    def borrow(self):
        pass

class Student(AbstractMember):
    def borrow(self):
        return "Student borrowing rules."

class Teacher(AbstractMember):
    def borrow(self):
        return "Teacher borrowing rules."

s = Student()
t = Teacher()
print(s.borrow())
print(t.borrow())
