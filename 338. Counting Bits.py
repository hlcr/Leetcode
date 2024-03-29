def countBits(num):
    result = [0 for _ in range(num+1)]
    for i in range(1, num+1):
        if i % 2 == 1:
            result[i] = result[i-1] + 1
        else:
            result[i] = result[i//2]
    return result[-1]
