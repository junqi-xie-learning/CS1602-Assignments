i = eval(input())
if i < 0:
    s = str(-i)
    s = s[::-1]
    i = int(i)
    print(-i)
else:
    s = str(i)
    s = s[::-1]
    i = int(s)
    print(i)