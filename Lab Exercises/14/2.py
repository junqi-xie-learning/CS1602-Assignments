i, n = int(input()), int(input())

l = []
while i >= n:
    l.append(i % n)
    i //= n
l.append(i)
l.reverse()

print("".join(str(i) for i in l))