class _pow:
    @classmethod
    def pow(cls, x, n):
        return x ** n

def main():
    x, n = int(input()), int(input())
    print(_pow.pow(x, n))

if __name__ == "__main__":
    main()