import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for x in range(int(math.sqrt(c))+1):

            y = math.sqrt(c - x**2)
            if int(y) == y:

                return True
        return False