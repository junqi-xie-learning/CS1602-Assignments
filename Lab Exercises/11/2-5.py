def generate_list(n):
    l = []
    for i in range (1, n + 1):
        l.append(i ** 2)
    return l

print(generate_list(20))
print(generate_list(20)[:5])
print(generate_list(20)[-1:-6:-1])
print(generate_list(20)[6::])