def square(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    return s

a, b, c = eval(input()), eval(input()), eval(input())
print(square(a, b, c))