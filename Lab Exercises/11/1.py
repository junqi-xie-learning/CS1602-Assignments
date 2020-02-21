def generate_dict(n):
    d = {}
    for i in range(1, n + 1):
        d[i] = i ** 2
    return d

d = generate_dict(20)
for i in d.keys():
    print(d[i])