def findLowerBound(target, nums):
    if not nums:
        return -1
    bottom = -1
    up = len(nums)
    while bottom + 1 < up:
        mid = bottom + (up - bottom) // 2
        if nums[mid] < target:
            bottom = mid
        else:
            up = mid
    return bottom + 1

if __name__ == '__main__':
    sortedArray = [0,1]
    r = findLowerBound(1, sortedArray)
    print(r)
