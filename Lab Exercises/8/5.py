def intersect(A, B):
    sA = set(A)
    sB = set(B)
    s = sA & sB
    if s == set():
        return False
    else: return list(s)

A, B = eval(input()), eval(input())
S = intersect(A, B)
if (not S):
    print("no intersection")
else: print(S)