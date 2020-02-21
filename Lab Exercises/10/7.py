import math

def angle(a, b, c):
    A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    B = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    C = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    return (A, B, C)

a, b, c = eval(input()), eval(input()), eval(input())
print(angle(a, b, c))