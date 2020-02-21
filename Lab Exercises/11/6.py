def dog_to_human(d):
    if d == 1:
        return 14
    elif d == 2:
        return 22
    else:
        return 22 + 5 * (d - 2)

d = int(input())
print(dog_to_human(d))