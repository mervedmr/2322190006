class Logger:
    def log(self, msg="Boş mesaj", prefix="INFO"):
        print(f"[{prefix}] {msg}")

    def multi(self, *msgs):
        for m in msgs:
            print(m)

logger = Logger()
logger.log("Kayıt alındı")
logger.multi("A","B","C")
