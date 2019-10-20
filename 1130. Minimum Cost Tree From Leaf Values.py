class Solution:
    def mctFromLeafValues(self, arr) -> int:
        result = 0
        while len(arr) > 1:
            r_border = len(arr)
            i = 1
            mp = float("inf")
            while i < r_border:
                if arr[i - 1] * arr[i] < mp:
                    mp = arr[i - 1] * arr[i]
                    l = i - 1
                    r = i
                i += 1

            r_border -= 1
            result += mp
            if arr[l] > arr[r]:
                arr.pop(r)
            else:
                arr.pop(l)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.mctFromLeafValues([6, 2, 4]))