class Array:
    def __init__(self, lst):
        self.array = lst

    def find_sum(self, target):
        for i in range(len(self.array)):
            for j in range(i):
                if self.array[i] + self.array[j] == target:
                    return (j + 1, i + 1)

def main():
    a = Array([10, 20, 10, 40, 50, 60, 70])
    print(a.find_sum(50))

if __name__ == "__main__":
    main()