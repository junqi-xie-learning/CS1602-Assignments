import math

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def square(self): # 计算这个三角形的面积
        p = (self.a + self.b + self.c) / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)
        return s

    def angle(self): # 计算各个角度的弧度值
        A = math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c))
        B = math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))
        C = math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b))
        return (A, B, C)

    def excircle(self): # 计算外接圆的半径和面积
        A = self.angle()[0]
        R = self.a / math.sin(A) / 2
        return (R, math.pi * R ** 2)

    def incircle(self): # 计算内接圆的半径和面积
        s = self.square()
        r = s * 2 / (self.a + self.b + self.c)
        return (r, math.pi * r ** 2)