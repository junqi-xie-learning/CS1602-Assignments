l = []
def f(n):
    for i in range(n + 1):
        if i == 0 or i == 1:
            l.append(i)
        else:
            l.append(l[i - 1] + l[i - 2])
    return l[-1]

n = int(input())
print(f(n))