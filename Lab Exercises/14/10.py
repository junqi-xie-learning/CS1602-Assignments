def sum(*args):
    r = 0
    for arg in args:
        r += arg
        return r 
 
print(sum(1, 3, 5))