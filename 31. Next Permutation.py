class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start):
            i, j = start, len(nums) - 1
            while (i < j):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if len(nums) < 2:
            return nums

        i = len(nums)-1
        j = i - 1
        while j >= 0:
            if nums[j] < nums[i]:
                k = i
                while k < len(nums) and nums[k] > nums[j]:
                    k += 1
                nums[k - 1], nums[j] = nums[j], nums[k - 1]
                reverse(nums, i)
                return nums
            i -= 1
            j -= 1


        reverse(nums, 0)
        return nums

if __name__ == '__main__':
    r = Solution().nextPermutation([3,2,1])
    print(r)