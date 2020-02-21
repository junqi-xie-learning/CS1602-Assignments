class Subset:
    def __init__(self, lst):
        self.int_set = lst

    def __find_subset(self, lst):
        if len(lst) == 0:
            return [[]]
        else:
            last = lst[-1]
            del lst[-1]
            result = self.__find_subset(lst)
            for l in result:
                result.append(l + [last])
            return result

    def subset(self):
        return self.__find_subset(self.int_set)

def main():
    s = Subset([4, 5, 6])
    print(s.subset())

if __name__ == "__main__":
    main()