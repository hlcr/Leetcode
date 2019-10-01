class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def helper(exist_list, rest, rest_k):
            if len(rest) < rest_k:
                return
            if len(exist_list) == k:
                result.append(exist_list)
                return
            i = 0
            while i < len(rest):
                next_exist_list = exist_list[:]
                next_exist_list.append(rest[i])
                helper(next_exist_list, rest[i + 1:], rest_k - 1)
                i += 1

        helper([], list(range(1, n + 1)), k)
        return result