university = {}

str1 = input("Please give me a university name and its belief:")
str2 = input("Please give me another university name and its belief:")

university[str1.split()[0]] = str1.split()[1]
university[str2.split()[0]] = str2.split()[1]

str3 = input("Please give me a university name:")
if str3 in university.key():
    print("{}'s belief is {}".format(str3, university[str3]))
else: print("I don't know {}'s belief.".format(str3))