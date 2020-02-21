def match(string, substring):
    count = 0
    for i in range(len(string)):
        if len(string) - i < len(substring):
            return count
        if string[i:i + len(substring)] == substring:
            count += 1

string = input("string: ")
substring = input("substring: ")
direction = int(input("direction: "))

print()
print("string: \"{}\"".format(string))
print("substring: \"{}\"".format(substring))

if direction == 0:
    print("direction: from left to right")
    print("number matched: {}".format(match(string, substring)))
else:
    print("direction: from right to left")
    reversed_substring = substring[::-1]
    print("reversed substring: \"{}\"".format(reversed_substring))
    print("number matched: {}".format(match(string, reversed_substring)))