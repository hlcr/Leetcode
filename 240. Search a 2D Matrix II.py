class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i, j = 0, 0
        width, height = len(matrix[0]), len(matrix)
        while i < height and j < width:
            while j + 1 < width and matrix[i][j + 1] <= target:
                j += 1
            width = j + 1

            print(matrix[i][j])
            if matrix[i][j] == target:
                return True

            i += 1
            j = 0

        return False


    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i, j = len(matrix)-1, 0
        width, height = len(matrix[0]), len(matrix)
        while i >= 0 and j < width:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1

        return False


if __name__ == '__main__':
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

    target = 19
    r = Solution().searchMatrix1(matrix, target)
    print(r)