import collections
def numFriendRequests(ages):
    """
    :type ages: List[int]
    :rtype: int
    """
    result = 0

    ages_dict = collections.Counter(ages)
    for k, v in ages_dict.items():
        if v != 1:
            r = 1
            for i in range(1, v + 1):
                r *= i
            result += r

    ages = sorted(list(ages_dict.keys()))

    for A, a in enumerate(ages):
        r = 0
        for B in range(A):
            if ages[B] > 0.5 * ages[A] + 7:
                r += ages_dict[ages[B]]
        result += ages_dict[ages[A]] * r
    return result


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ret = [0] * 121
        for age in ages:
            ret[age] = ret[age] + 1
        count = 0
        for ageA, countA in enumerate(ret):
            for ageB, countB in enumerate(ret):
                if (self.helper(ageA, ageB) == True):
                    count += countA * countB
                    if (ageA == ageB):
                        count -= countA
        return count

    def helper(self, ageA, ageB):
        if (ageB <= (0.5 * ageA + 7) or ageB > ageA or (ageB > 100 and ageA < 100)):
            return False
        else:
            return True

s = Solution()
r = s.numFriendRequests([14,14])
print(r)
print(numFriendRequests([14,14,16,16,16]))