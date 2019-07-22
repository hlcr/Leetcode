class Solution:
    def largestSumOfAverages(self, A, K):
        S = [0]
        for n in A:
            S.append(S[-1] + n)
        average = lambda i, j: (S[j] - S[i]) / (j - i)
        l = len(A)

        dp = [average(i, l) for i in range(l)]
        print(dp)

        for k in range(K - 1):
            for i in range(l):
                for j in range(i + 1, l):
                    dp[i] = max(dp[i], dp[j] + average(i, j))
                print(dp)

        return dp[0]

# Solution().largestSumOfAverages([4,1,7,5,6,2,3], 4)
Solution().largestSumOfAverages([9,1,2,3,9], 3)

