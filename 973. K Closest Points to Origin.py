class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        import heapq
        class myHeap:
            def __init__(self, data):

                self._data = [(self.fn(d), d) for d in data]
                heapq.heapify(self._data)

            def fn(self, d):
                return d[0] * d[0] + d[1] * d[1]

            def pop(self):
                return heapq.heappop(self._data)[1]

            def push(self, data):
                heapq.heappush(self._data, (self.fn(data), data))

        if len(points) <= K:
            return points
        heap = myHeap(points)
        result = []
        for k in range(K):
            result.append(heap.pop())
        return result


if __name__ == '__main__':
    data = [[3,3],[5,-1],[-2,4]]
    K = 2
    # r = Solution().kClosest(data, K)
    data.sort(key=lambda x: x[0]*x[0] + x[1]*x[1])
    print(data[:K])