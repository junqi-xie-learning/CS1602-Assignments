def sum(l):
    s = 0
    for i in l:
        if type(i) == list:
            s += sum(i)
        else:
            s += i
    return s

l = eval(input())
print(sum(l))