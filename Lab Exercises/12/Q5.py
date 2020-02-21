class Array:
    def __init__(self, lst):
        self.array = lst

    def find_sum(self):
        result = []
        for i in range(len(self.array)):
            for j in range(i):
                for k in range(j):
                    if self.array[i] + self.array[j] + self.array[k] == 0:
                        result.append([self.array[i], self.array[j], self.array[k]])
        return result

def main():
    a = Array([-25, -10, -7, -3, 2, 4, 8, 10])
    print(a.find_sum())

if __name__ == "__main__":
    main()