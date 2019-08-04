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
                sec = stack.pop()
            stack.append(num)
            print(stack)
        return False

if __name__ == '__main__':
    Solution().find132pattern([4,5,6,7,2,3,4,6,0,1,5])
