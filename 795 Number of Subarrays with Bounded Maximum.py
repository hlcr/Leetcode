def numSubarrayBoundedMax(A, L, R):
    """
    :type A: List[int]
    :type L: int
    :type R: int
    :rtype: int
    """
    pre = 0
    temp = 0
    result = 0
    for a in A:
        if a < L:
            temp += 1
        if a >= L and a <= R:
            temp += 1
            if pre != 0:
                result += (temp - pre)
            pre = temp
            result += pre
        if a > R:
            if pre != 0:
                result += (temp - pre)
            pre = 0
            temp = 0

    return result

print(numSubarrayBoundedMax([2,9,2,5,6], 2, 8))