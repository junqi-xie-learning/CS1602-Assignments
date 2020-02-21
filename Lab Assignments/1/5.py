class EquilateralTriangle:
    def __init__(self, i):
        self.length = i

    def height(self):
        return self.length * (3 ** (1 / 2) / 2)

    def area(self):
        return self.length * self.height() / 2

tri1 = EquilateralTriangle(2)  # side length is 2
print(tri1.area())
print(tri1.height())