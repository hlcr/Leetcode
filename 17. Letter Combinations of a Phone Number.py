class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        output = []

        def recursive(comb, next_digits):
            if len(next_digits) == 0:
                output.append(comb)
            else:
                for c in phone[next_digits[0]]:
                    recursive(comb+c, next_digits[1:])

        recursive("", digits)
        return output

if __name__ == '__main__':
    l = Solution().letterCombinations("345")
    print(l)
