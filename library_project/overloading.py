from functools import singledispatchmethod

class Calc:
    @singledispatchmethod
    def area(self, data):
        raise NotImplementedError

    @area.register
    def _(self, r: float):
        return 3.14 * r * r

    @area.register
    def _(self, rect: tuple):
        w, h = rect
        return w * h

c = Calc()
print(c.area(3.0))
print(c.area((2,3)))
