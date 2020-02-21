import math

def square(a, b, c): # 计算这个三角形的面积
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    return s

def angle(a, b, c): # 计算各个角度的弧度值
    A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    B = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    C = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    return (A, B, C)

def excircle(a, b, c): # 计算外接圆的半径和面积
    A = angle(a, b, c)[0]
    R = a / math.sin(A) / 2
    return (R, math.pi * R ** 2)

def incircle(a, b, c): # 计算内接圆的半径和面积
    s = square(a, b, c)
    r = s * 2 / (a + b + c)
    return (r, math.pi * r ** 2)