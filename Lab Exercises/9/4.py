string = ""
l = []
while string != "end":
    string = input()
    l.append(string)

for string in l:
    if string != "end":
        print(string.upper())