def measure_min_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def convert2pair(num_list, w):
    result = []
    for nums in num_list:
        temp = [(num // w, num % w) for num in nums]
        flag = True
        for i in range(len(temp)):
            if not flag:
                break
            for j in range(i + 1, len(temp)):
                m = measure_min_distance(temp[i], temp[j])
                if m <= 2:
                    flag = False
                    break
        if flag:
            result.append(temp)
    return result


import queue


def get_distance(square_list, h, w):
    long_distance = h * w
    matrix = [[long_distance for _ in range(w)] for _ in range(h)]
    is_visited = [[False for _ in range(w)] for _ in range(h)]
    q = queue.Queue()
    max_len = 0
    for x, y in square_list:
        matrix[x][y] = 0
        is_visited[x][y] = True
        q.put((x, y))

    while not q.empty():
        cx, cy = q.get()
        for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = cx + i, cy + j
            if 0 <= ny < w and 0 <= nx < h:
                if matrix[nx][ny] > (matrix[cx][cy] + 1):
                    matrix[nx][ny] = matrix[cx][cy] + 1
                    max_len = max(max_len, matrix[nx][ny])
                    q.put((nx, ny))
    return max_len


def combine(k, h, w):
    if h*w <= k:
        return 0

    result = []
    n = h * w
    min_distance = 99

    def helper(exist_list, rest, rest_k):
        if len(rest) < rest_k:
            return
        if len(exist_list) == k:
            result.append(exist_list)
            return
        i = 0
        while i < len(rest):
            next_exist_list = exist_list[:]
            next_exist_list.append(rest[i])
            helper(next_exist_list, rest[i + 1:], rest_k - 1)
            i += 1

    helper([], list(range(n)), k)
    result = convert2pair(result, w)
    if not result:
        return 1

    for points in result:
        distance = get_distance(points, h, w)
        if min_distance > distance:
            min_distance = min(min_distance, distance)

            print(points, min_distance)
            if min_distance == 1:
                return 1

    print(min_distance)
    return min_distance



if __name__ == '__main__':
    print(combine(2, 1, 3))





