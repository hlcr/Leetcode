class Solution:

    def update_neighbors(self, co):
        x, y = co[0], co[1]
        for op in self.ops:
            xi, yi = x + op[0], y + op[1]
            if xi >= 0 and xi < self.h and yi >= 0 and yi < self.w:
                if self.r[xi][yi] == 9999:
                    self.queue.append((xi, yi))
                    self.r[xi][yi] = self.r[x][y] + 1

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.queue = []
        self.ops = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.r = [[9999 for _ in range(self.w)] for _ in range(self.h)]

        for i in range(self.h):
            for j in range(self.w):
                if matrix[i][j] == 0:
                    self.r[i][j] = 0
                    self.queue.append((i, j))

        while self.queue:
            co = self.queue.pop(0)
            self.update_neighbors(co)
        return self.r
