class Reversed_string:
    def __init__(self, s):
        self.orig = s.split()

    def output(self):
        return ' '.join(reversed(self.orig))

def main():
    r = Reversed_string('hello .py')
    print(r.output())

if __name__ == "__main__":
    main()