class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __le__(self, value):
        return self.a < value.a or self.a == value.a and self.b < value.b \
            or self.a == value.a and self.b == value.b and self.c <= value.c

    def __ge__(self, value):
        return self.a > value.a or self.a == value.a and self.b > value.b \
            or self.a == value.a and self.b == value.b and self.c >= value.c

    def __lt__(self, value):
        return not self.__ge__(value)

    def __gt__(self, value):
        return not self.__le__(value)

    def __eq__(self, value):
        return self.a == value.a and self.b == value.b and self.c == value.c

    def __ne__(self, value):
        return not self.__eq__(value)

    def __str__(self):
        return "({}, {}, {})".format(self.a, self.b, self.c)

def main():
    a1, b1, c1 = int(input()), int(input()), int(input())
    a2, b2, c2 = int(input()), int(input()), int(input())
    t1, t2 = Triangle(a1, b1, c1), Triangle(a2, b2, c2)
    print(t1 <= t2, t1 < t2, t1 >= t2, t1 > t2, t1 == t2, t1 != t2)
    print(t1, t2)

if __name__ == "__main__":
    main()