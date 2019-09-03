class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        signal = True
        while i >= 0 and signal:
            if digits[i] + 1 < 10:
                signal = False
            digits[i] = (digits[i] + 1) % 10
            i -= 1
        if signal:
            return [1] + digits
        else:
            return digits

if __name__ == '__main__':
    r = Solution().plusOne([0])
    print(r)