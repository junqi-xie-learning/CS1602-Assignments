def sumDigits(i):
    if i <= 9:
        return i
    else:
        return i % 10 + sumDigits((i - i % 10) // 10)

i = int(input())
print(sumDigits(i))