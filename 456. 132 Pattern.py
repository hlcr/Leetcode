class Solution:
    def find132pattern(self, nums):
        if not nums:
            return False
        stack = []
        sec = float('-inf')
        for num in nums[::-1]:
            if num < sec:
                return True
            while stack and stack[-1] < num:
                # sec = max(sec, stack.pop())
                sec = stack.pop()
            stack.append(num)
        return False

    def find132pattern1(self, nums):
        if not nums:
            return False
        stack = [float('-inf'),float('-inf')]
        sec = float('-inf')
        for num in nums[::-1]:
            print(stack, sec, num)
            if num < sec:
                return True
            if stack[-1] < num:
                stack.append(num)
                sec = stack[-2]
            # stack.append(num)

        return False


    def find132pattern2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        minValues = [nums[0]]
        index = 1
        min = nums[0]
        max = nums[0]
        count = len(nums)
        while index < count:
            n = nums[index]

            if n >= max:
                max = n
            elif n <= min:
                min = n
            else:
                cIndex = index - 1
                while cIndex > 0:
                    if (nums[cIndex] > n):
                        if (minValues[cIndex] < n):
                            return True
                    if minValues[cIndex] > n:
                        break
                    cIndex -= 1

            minValues.append(min)
            index += 1

        return False





if __name__ == '__main__':
    r = Solution().find132pattern1([1,7,6,5,4,3])
    print(r)
