def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

a, b, c = eval(input()), eval(input()), eval(input())
print(is_triangle(a, b, c))