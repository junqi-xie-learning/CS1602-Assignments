i = int(input("Input: "))
o = 0

while i != 0:
    o = o * 10 + i % 10
    i //= 10

print("Output: {}".format(o))