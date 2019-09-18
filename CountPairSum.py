


class Solution:
    def find_pair_num(self, array, target):
        r_set = set()
        result = []
        for n in array:
            if n not in r_set:
                if target - n in r_set:
                    result.append((n, target - n))
                r_set.add(n)
        print(result)
        return r_set

    def closet_two_sum(self, array, target):
        array.sort()
        i, j = 0, len(array)-1
        result = 0
        while i < j:
            temp = array[i] + array[j]
            if target - temp > 0:
                result = max(result, temp)
                i += 1
            elif target == temp:
                return result
            else:
                j -= 1
        print(result)
        return result


    def union(self, nums):
        import heapq
        heapq.heapify(nums)
        result = 0
        while len(nums) > 1:
            r1 = heapq.heappop(nums)
            r2 = heapq.heappop(nums)
            r = r1 + r2
            result += r
            heapq.heappush(nums, r)
        print(result)
        return result




if __name__ == '__main__':
    # nums = [1, 1, 2, 45, 46, 46]
    # nums = [1, 5, 1, 5]
    # target = 6
    # Solution().find_pair_num(nums, target)

    nums = [90, 85, 75, 60, 120, 150, 125]
    target = 220
    Solution().closet_two_sum(nums, target)

    Solution().union([20, 4, 8, 2])
    Solution().union([1, 2, 5, 10, 35, 89])

