class Notifier:
    def send(self, msg):
        print("NOTIFY:", msg)

class Library:
    def lend(self, book, notifier: Notifier):
        notifier.send(f"{book} ödünç verildi")

lib = Library()
notifier = Notifier()
lib.lend("1984", notifier)
