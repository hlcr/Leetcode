class Solution(object):
    def rob_helper(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        m1 = self.rob_helper(nums[: n - 1])
        m2 = self.rob_helper(nums[1:])
        return max(m1, m2)
