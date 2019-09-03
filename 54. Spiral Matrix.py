class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        i1 = 0
        i2 = len(matrix) - 1
        j1 = 0
        j2 = len(matrix[0]) - 1
        result = []

        while i1 <= i2 and j1 <= j2:
            for j in range(j1, j2 + 1):
                result.append(matrix[i1][j])
            i1 += 1

            for i in range(i1, i2 + 1):
                result.append(matrix[i][j2])
            j2 -= 1

            if i1 <= i2:
                for j in range(j2, j1 - 1, -1):
                    result.append(matrix[i2][j])
                i2 -= 1

            if j1 <= j2:
                for i in range(i2, i1 - 1, -1):
                    result.append(matrix[i][j1])
                j1 += 1

        return result

if __name__ == '__main__':
    r = Solution().spiralOrder([[0],[1],[2]])
    print(r)