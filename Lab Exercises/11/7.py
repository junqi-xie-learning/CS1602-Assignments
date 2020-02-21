import math

def find_prime(n):
    is_prime = []
    prime = []
    for i in range(n + 1):
        is_prime.append(True)
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i ** 2, n + 1, i):
                is_prime[j] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)
    return prime

print(find_prime(1000000))