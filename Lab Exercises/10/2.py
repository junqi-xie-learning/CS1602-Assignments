import string

def count_char(sentence):
    letter = 0
    digit = 0
    for i in range(len(sentence)):
        if sentence[i] in string.ascii_letters:
            letter += 1
        elif sentence[i] in string.digits:
            digit += 1
    return (letter, digit)

sentence = input()
letter, digit = count_char(sentence)
print("LETTERS {}".format(letter))
print("DIGITS {}".format(digit))