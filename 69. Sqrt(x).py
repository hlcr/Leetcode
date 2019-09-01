class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x//r) // 2
        return int(r)


if __name__ == '__main__':
    r = Solution().mySqrt(16)
    print(r)
