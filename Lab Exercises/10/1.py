def factortial(i):
    f = 1
    for i in range(1, i + 1):
            f *= i
    return f

i = int(input())
print(factortial(i))