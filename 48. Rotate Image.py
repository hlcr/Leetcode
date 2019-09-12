class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            start = 0
            end = len(matrix) - 1

            while start < end:
                matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
                start += 1
                end -= 1

if __name__ == '__main__':
    r = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    for k in r:
        print(k)
    print()
    Solution().rotate(r)
    print()
    for l in r:
        print(l)