from dataclasses import dataclass

@dataclass(frozen=True)
class ISBN:
    code: str

isbn = ISBN("123-456")
print(isbn)
