import math

a, b, c = float(input()), float(input()), float(input())
print(a + b > c and a + c > b and b + c > a) # 判断给定的三个数 a, b, c 能不能构成一个三角形

p = (a + b + c) / 2 # 计算这个三角形的面积
s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
print("{:.3f}".format(s))

A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) # 计算各个角度的弧度值
B = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
C = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
print("A = {:.3f}".format(A))
print("B = {:.3f}".format(B))
print("C = {:.3f}".format(C))

R = a / math.sin(A) / 2 # 计算外接圆的半径和面积
print("{:.3f}".format(R))
print("{:.3f}".format(math.pi * R ** 2))

r = s * 2 / (a + b + c) # 计算内接圆的半径和面积
print("{:.3f}".format(r))
print("{:.3f}".format(math.pi * r ** 2))