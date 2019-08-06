class Solution:
    def addToArrayForm(self, A, K):
        r = 0
        for a in A:
            r = r * 10 + a
        r += K
        print(r)
        l = []
        if r == 0:
            return [0]
        while r != 0:
            l.insert(0, r % 10)
            r //= 10
        return l

if __name__ == '__main__':
    r = Solution().addToArrayForm([1,3,4], 54)

    print(divmod(125, 10))
    print(r)