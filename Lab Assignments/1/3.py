def upperToLower(char):
    difference = ord('a') - ord('A')
    return chr(ord(char) + difference)

print(upperToLower('A'))
print(upperToLower('Z'))