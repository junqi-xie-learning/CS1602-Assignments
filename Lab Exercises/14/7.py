def search(L, x):
    n = len(L)
    if L[n // 2] == x:
        return n // 2
    elif L[n // 2] < x:
        return search(L[n // 2 + 1:n], x) + n // 2 + 1
    else:
        return search(L[:n // 2], x)

L = eval(input())
x = int(input())
print(search(L, x))