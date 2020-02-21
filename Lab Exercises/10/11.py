def eval_int(i):
    if i % 2 == 0:
        return "It is an even number"
    else: return "It is an odd number"

i = int(input())
print("\"{}\"".format(eval_int(i)))