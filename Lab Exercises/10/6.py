def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    if y % 400 == 0:
        return True
    return False

y = int(input())
print(is_leap_year(y))