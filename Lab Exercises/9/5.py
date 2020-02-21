def check_digit(n):
    for i in range(4):
        if n % 2 != 0:
            return False
        n //= 10
    return True

l = []
for i in range(1000, 3001):
    if check_digit(i):
        l.append(i)

print(", ".join([str(i) for i in l]))