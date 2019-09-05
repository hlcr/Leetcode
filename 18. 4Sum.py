class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        result = []
        nums.sort()
        print(nums)
        for i in range(len(nums) - 3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                bottom = j + 1
                up = len(nums) - 1
                partial_sum = nums[i] + nums[j]
                while bottom < up:
                    if partial_sum + nums[bottom] + nums[up] < target:
                        bottom += 1
                    elif partial_sum + nums[bottom] + nums[up] > target:
                        up -= 1
                    else:
                        result.append([nums[i], nums[j], nums[bottom], nums[up]])
                        while bottom + 1 <= up and nums[bottom + 1] == nums[bottom]:
                            bottom += 1
                        while up - 1 >= bottom and nums[up - 1] == nums[up]:
                            up -= 1
                        bottom += 1
                        up -= 1
        return result


if __name__ == '__main__':

    r = Solution().fourSum(
[0,0,0,0], 0)
    print(r)


