from queue import Queue


def find_path(t_map):
    step = [[999 for _ in range(len(t_map[0]))] for _ in range(len(t_map))]
    queue = []
    result = 999
    for i in range(len(t_map)):
        for j in range(len(t_map[0])):
            if t_map[i][j] == 'S':
                queue.append((i, j))
                step[i][j] = 1

    while queue:
        cn = queue.pop(0)
        x1, y1 = cn
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i != 0 and j != 0:
                    continue
                x = x1 + i
                y = y1 + j
                if x >= 0 and x < len(t_map[0]) and y >=0 and y < len(t_map):
                    if t_map[x][y] == 'O' and step[x][y] > (step[x1][y1] + 1):
                        step[x][y] = step[x1][y1] + 1
                        queue.append((x, y))
                    elif t_map[x][y] == 'X':
                        step[x][y] = min(step[x1][y1] + 1, step[x][y])
                        result = min(result, step[x][y])
    for s in step:
        print(s)
    return result






if __name__ == '__main__':
    t_map = [
    ['S', 'O', 'O', 'S', 'S'],
    ['D', 'O', 'D', 'O', 'D'],
    ['O', 'O', 'O', 'O', 'X'],
    ['X', 'D', 'D', 'O', 'O'],
    ['X', 'D', 'D', 'D', 'O'],
    ]
    r = find_path(t_map)
    print(r)

