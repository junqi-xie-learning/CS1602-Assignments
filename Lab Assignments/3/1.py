import random

s = 20
n = 8
print("s = {}".format(s))
w = random.sample(range(1, 26), n)
print("w = {}".format(w))
print()

selected = []
def knap(s0, n0):
    if s0 == 0:
        return True
    elif s0 < 0 or s0 > 0 and n0 <= 0:
        return False
    
    if knap(s0 - w[n0 - 1], n0 - 1):
        selected.append(w[n0 - 1])
        return True
    return knap(s0, n0 - 1)

if knap(s, n):
    print("There is a solution.")
    print("20 = ", end = '')
    print(" + ".join([str(i) for i in selected]))
else:
    print("There is no solution.")