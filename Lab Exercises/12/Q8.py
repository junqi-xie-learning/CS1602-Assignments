class String:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input()

    def print_String(self):
        print(self.s.upper())

def main():
    s = String()
    s.get_String()
    s.print_String()

if __name__ == "__main__":
    main()