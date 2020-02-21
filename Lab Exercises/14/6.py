def pow(x, n):
    if n == 0:
        return 1
    else:
        return x * pow(x, n - 1)

x, n = int(input()), int(input())
print(pow(x, n))