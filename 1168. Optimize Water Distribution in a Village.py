class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        if not pipes:
            return sum(wells)

        ufl = [-1 for _ in range(n + 1)]

        def find(m):
            if ufl[m] != -1:
                ufl[m] = find(ufl[m])
            elif ufl[m] == -1:
                return m
            return ufl[m]

        for index, well in enumerate(wells):
            pipes.append([0, index + 1, well])
        pipes.sort(key=lambda x: x[-1])
        result = 0
        count = 0
        for pipe in pipes:
            h1 = pipe[0]
            h2 = pipe[1]
            s1 = find(h1)
            s2 = find(h2)

            if s1 != s2:
                ufl[s1] = s2
                result += pipe[2]
                count += 1
            if count >= n:
                break
        return result

