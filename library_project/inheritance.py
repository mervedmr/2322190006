class Member:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Member: {self.name}"

class Student(Member):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def info(self):
        base = super().info()
        return f"{base} - Grade: {self.grade}"

class Teacher(Member):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def info(self):
        base = super().info()
        return f"{base} - Subject: {self.subject}"

print(Student("Alice", "10th").info())
print(Teacher("Bob", "Math").info())
