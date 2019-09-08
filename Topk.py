import heapq

class Solution:


    def getTopK(self, location, data, k):

        class MyHeap:
            def __init__(self, initial, ml):
                self.m = ml[0]
                self.n = ml[1]
                if initial:
                    self._data = [(self.fn(item), item) for item in initial]
                    heapq.heapify(self._data)
                else:
                    self._data = []

            def fn(self, item):
                m = self.m
                n = self.n
                p = item[0]
                q = item[1]
                return (m - p) * (m - p) + (n - q) * (n - q)

            def push(self, item):
                heapq.heappush(self._data, (self.fn(item), item))

            def pop(self):
                return heapq.heappop(self._data)[1]

        mh = MyHeap(data, location)
        result = []
        for _ in range(k):
            r = mh.pop()
            result.append(r)
        return result

if __name__ == '__main__':
    po = [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
    s = Solution()
    r = s.getTopK([0, 0], po, 3)
    print(r)
