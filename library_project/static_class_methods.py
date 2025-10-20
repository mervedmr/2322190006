class Library:
    registry = {}

    def __init__(self, name):
        self.name = name

    @classmethod
    def register(cls, key, library):
        cls.registry[key] = library

    @staticmethod
    def library_info():
        return "Library holds books and members."

lib = Library("City Library")
Library.register("city", lib)
print(Library.library_info())
