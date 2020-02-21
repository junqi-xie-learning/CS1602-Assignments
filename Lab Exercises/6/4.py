import my_class

a, b, c = eval(input()), eval(input()), eval(input())
t = my_class.Triangle(a, b, c)
print(t.square())
print(t.angle())
print(t.excircle())
print(t.incircle())