class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.num = num
        self.total_length = len(num)
        length = len(num) // 2 + 2
        i = 1
        while i < length:
            if num[0] == '0' and i != 1:
                return False
            for j in range(i + 1, self.total_length):
                if num[i:i + 1] == '0' and j - i != 1:
                    i += 1
                    if i > length:
                        return False
                    continue
                if self.dfs(num[:i], num[i:j], j):
                    return True
            i += 1
        return False

    def dfs(self, first, second, index):
        third = str(int(first) + int(second))

        # print(first,second,third, self.num.find(third, index) == index)
        if self.num.find(third, index) == index:
            if index + len(third) == self.total_length :
                return True
            if self.dfs(second, third, index + len(third)):
                return True

        return False

if __name__ == '__main__':
    r = Solution().isAdditiveNumber("198019823962")
    print(r)