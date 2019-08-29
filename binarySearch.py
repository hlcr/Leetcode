def findLowerBound(target, nums):
    if not nums:
        return -1
    lb = -1
    ub = len(nums)
    while lb + 1 < ub:
        mid = lb + (ub - lb) // 2
        if nums[mid] < target:
            lb = mid
        else:
            ub = mid
    return lb + 1


if __name__ == '__main__':
    sortedArray = [1, 2, 2, 3, 4, 6, 6, 6, 13, 18]
    r = findLowerBound(19, sortedArray)
    print(r)
