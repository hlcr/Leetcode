def find_path(t_map):
    queue = [(0,0)]
    step = [[999 for _ in range(len(t_map[0]))] for _ in range(len(t_map))]
    step[0][0] = 0
    rx, ry = 99,99
    for s in step:
        print(s)


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
                        rx, ry = x, y

    print(step[rx][ry])
    for s in step:
        print(s)
    # return step[rx][ry]


if __name__ == '__main__':
    find_path([
['O', 'O', 'O', 'O'],
['D', 'O', 'D', 'O'],
['O', 'O', 'O', 'O'],
['X', 'D', 'D', 'O'],
])