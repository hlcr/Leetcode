def search(matrix):
    queue = []
    nt = 0

    dm = [[9999 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                queue.append((i, j))
                dm[i][j] = 1
            # elif matrix[i][j] == 'X':
            #     nt += 1

    is_find = False

    while not is_find and queue:
        i, j = queue.pop(0)
        for k in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                if k == 0 or l == 0:
                    if 0 <= i + k < len(matrix) and 0 <= j + l < len(matrix[0]) and matrix[i+k][j+l] != 'D':
                        dm[i+k][j+l] = min(dm[i+k][j+l], dm[i][j] + 1)
                        if matrix[i+k][j+l] == 'X':
                            print(i+k, j+l)
                            return dm[i+k][j+l]
                        elif matrix[i+k][j+l] == 'O':
                            queue.append((i+k, j+l))



if __name__ == '__main__':
    my_map = [['S', 'O', 'O', 'S', 'S'],
     ['D', 'O', 'D', 'O', 'D'],
     ['O', 'O', 'O', 'O', 'X'],
     ['X', 'D', 'D', 'O', 'O'],
     ['X', 'D', 'D', 'D', 'O']]
    r = search(my_map)
    print(r)