from abc import ABC, abstractmethod

class SearchEngine(ABC):
    @abstractmethod
    def search(self, query): pass

class SimpleSearch(SearchEngine):
    def search(self, query):
        return f"{query} için arama yapıldı"

print(SimpleSearch().search("1984"))
