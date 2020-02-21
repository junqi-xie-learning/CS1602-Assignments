def remove_duplicate(l):
    lst = []
    for i in l:
        if i not in lst:
            lst.append(i)
    return lst

l = eval(input())
print(remove_duplicate(l))