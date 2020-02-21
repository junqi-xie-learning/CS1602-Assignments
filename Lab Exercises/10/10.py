def longer(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str2) > len(str1):
        return str2
    else: return "{}\n{}".format(str1, str2)

str1, str2 = input(), input()
print(longer(str1, str2))