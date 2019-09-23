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

def binary_search(target, nums):
    i = -1
    j = len(nums)
    while i + 1 < j:
        mid = i + (j - i) // 2
        if nums[mid] < target:
            i = mid
        else:
            j = mid
    return i +1



if __name__ == '__main__':
    sortedArray = [0,1,1,2,3,4,5]
    r = binary_search(2, sortedArray)
    print(r)
