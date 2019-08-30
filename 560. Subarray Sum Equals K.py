class Solution:
    def subarraySum(self, nums, k):
        if not nums:
            return 0
        result_map = dict()
        result_map[0] = 1
        ss = 0
        rr = 0
        for num in nums:
            ss += num
            if (ss - k) in result_map.keys():
                rr += 1
            if ss in result_map.keys():
                result_map[ss] = result_map[ss] + 1
            else:
                result_map[ss] = 1
        return rr

if __name__ == '__main__':
    r = Solution().subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    print(r)
