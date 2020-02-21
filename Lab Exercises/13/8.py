numbers = input().split(',')
print(", ".join(i for i in numbers if eval("0b{}".format(i)) % 5 == 0))