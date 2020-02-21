class Roman:
    def __init__(self, s):
        self.numeral = s
        self.values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

    def to_int(self):
        value = 0
        for i in range(len(self.numeral)):
            if self.numeral[i] in ('C', 'X', 'I') and \
                i + 1 != len(self.numeral) and \
                self.values[self.numeral[i]] < self.values[self.numeral[i + 1]]:
                value -= self.values[self.numeral[i]]
            else:
                value += self.values[self.numeral[i]]
        return value

def main():
    s = input()
    r = Roman(s)
    print(r.to_int())

if __name__ == "__main__":
    main()
