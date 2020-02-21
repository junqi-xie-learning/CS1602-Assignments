class Parentheses_validity:
    left1, right1 = '(', ')'
    left2, right2 = '{', '}'
    left3, right3 = '[', ']'

    def __init__(self, s):
        self.string = s
        self.__temp = []

    def __is_left(self, ch):
        return ch == self.left1 or ch == self.left2 or ch == self.left3

    def __is_right(self, ch):
        return ch == self.right1 or ch == self.right2 or ch == self.right3
    
    def __is_matched(self, left, right):
        return left == self.left1 and right == self.right1 \
            or left == self.left2 and right == self.right2 \
            or left == self.left3 and right == self.right3

    def validity_check(self):
        for ch in self.string:
            if self.__is_left(ch):
                self.__temp.append(ch)
            elif self.__is_right(ch):
                if self.__is_matched(self.__temp[-1], ch):
                    del self.__temp[-1]
                else: return False
        return self.__temp == []

def main():
    s = input()
    p = Parentheses_validity(s)
    print(p.validity_check())

if __name__ == "__main__":
    main()