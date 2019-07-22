def numFactoredBinaryTrees(A):

    A.sort()
    a_set = set(A)
    result_dict = dict()
    for a in A:
        result_dict[a] = 1

    for i in range(len(A)):
        right = A[i]
        for j in range(i):
            left = A[j]
            if left * right in a_set:
                result_dict[left * right] += 2 * result_dict[left] * result_dict[right]
        if right * right in a_set:
            result_dict[right * right] += result_dict[right] * result_dict[right]

    result_sum = 0
    for k, v in result_dict.items():
        result_sum += v
    return result_sum

def numFactoredBinaryTrees1(A):
    MOD = 10 ** 9 + 7
    N = len(A)
    A.sort()
    dp = [1] * N
    index = {x: i for i, x in enumerate(A)}
    for i, x in enumerate(A):
        for j in range(i):
            if x % A[j] == 0: #A[j] will be left child
                right = x / A[j]
                if right in index:
                    dp[i] += dp[j] * dp[index[right]]
                    dp[i] %= MOD

    return sum(dp) % MOD

l = [45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48]
r = numFactoredBinaryTrees(l)
print(r)
r = numFactoredBinaryTrees1(l)
print(r)



