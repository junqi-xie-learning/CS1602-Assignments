import math

def is_square(i):
    root = math.sqrt(i)
    return root == int(root)

u, v = input("Input: ").split()
u, v = int(u), int(v)

array = [u + v]
m = 1
n = 1
s = u + v
while not (s > 10000 and is_square(s)):
    if n % 2 != 0:
        array.append(array[m - 1] + u)
    else:
        array.append(array[m - 1] + v)
        m += 1
    s += array[n]
    n += 1
print("Output: {}".format(s))