class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        while N > 0:
            pl = [i for i in cells]
            for i in range(1, len(cells) - 1):
                cells[i] = 1 if (pl[i - 1] + pl[i + 1]) % 2 == 0 else 0
            cells[0], cells[-1] = 0, 0
            # print(cells)
            N = (N - 1) % 14
        return cells
