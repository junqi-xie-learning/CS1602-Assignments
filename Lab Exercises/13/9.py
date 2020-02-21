import math

C = 50
H = 30
D_list = [int(i) for i in input().split(',')]
print(", ".join(str(round(math.sqrt(((2 * C * D) / H)))) for D in D_list))