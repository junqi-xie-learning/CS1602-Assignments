def gcd(a, b):
    if b == 0:
        return a
    return gcd(min(a, b), max(a, b) % min(a, b))

a, b = int(input()), int(input())
print(gcd(a, b))