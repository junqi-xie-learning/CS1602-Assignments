A = eval(input())
for i in range(1, len(A) - 1):
    if A[i - 1] <= A[i] and A[i] >= A[i + 1]:
        break
print(i)