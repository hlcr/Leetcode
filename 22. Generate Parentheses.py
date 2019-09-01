class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def helper(ln, rn, s):
            if ln < rn:
                helper(ln, rn-1, s+")")
            if ln != 0:
                helper(ln-1, rn, s+"(")
            if ln == 0 and rn == 0:
                result.append(s)
        helper(n, n, "")
        return result

if __name__ == '__main__':
    r = Solution().generateParenthesis(3)
    print(r)