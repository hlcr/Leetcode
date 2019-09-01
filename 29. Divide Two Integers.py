class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        res = 0
        m, n = abs(dividend), abs(divisor)

        while m >= n:
            print(m,n)
            t, i = n, 1
            while t << 1 < m:
                t <<= 1
                i <<= 1
            m -= t
            res += i

        if sign < 0:
            res = -res

        temp = 2 ** 31 - 1
        return temp if res > temp else res


if __name__ == '__main__':
    Solution().divide(10,3)