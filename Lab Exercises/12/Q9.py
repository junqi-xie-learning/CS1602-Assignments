class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def main():
    l, w = eval(input()), eval(input())
    r = Rectangle(l, w)
    print(r.area())

if __name__ == "__main__":
    main()