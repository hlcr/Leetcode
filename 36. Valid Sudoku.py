class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        height = len(board)
        width = len(board[0])

        for i in range(width):
            num_set = set()
            for j in range(height):
                num = board[i][j]
                if num == '.':
                    continue
                if num in num_set:
                    return False
                else:
                    num_set.add(num)

        for i in range(width):
            num_set = set()
            for j in range(height):
                num = board[j][i]
                if num == '.':
                    continue
                if num in num_set:
                    return False
                else:
                    num_set.add(num)

        for i in range(1,10,3):
            for j in range(1,10,3):
                num_set = set()
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        num = board[i+k][j+l]
                        if num == '.':
                            continue
                        if num in num_set:
                            return False
                        else:
                            num_set.add(num)
        return True
