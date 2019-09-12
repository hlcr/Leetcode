class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        result = s[0]
        max_len = 1
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
                max_len = 2
                result = s[i: i+2]
            else:
                dp[i][i + 1] = 0

        i = len(s) - 3

        while i >= 0:
            j = i + 2
            while j < len(s):
                if dp[i+1][j-1] > 0 and s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        result = s[i: j+1]
                j += 1
            i -= 1

        # for d in dp:
        #     print(d)
        # print(result)
        return result

if __name__ == '__main__':
    Solution().longestPalindrome("babad")

