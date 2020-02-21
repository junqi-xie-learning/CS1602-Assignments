i = int(input())

output = {}
for i in range(1, i + 1):
    output.update({i: i*i})

print(output)