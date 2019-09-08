def pick_points(data, sn):
    data1 = [(i, p) for i, p in enumerate(data)]
    data1.sort(key=lambda x: x[0])
    i = 0
    j = len(data) - 1
    rsm = 0
    p_index = (0,0)
    while i < j:
        temp_sum = data1[i][1] + data1[j][1]
        if temp_sum < sn:
            if temp_sum > rsm:
                rsm = temp_sum
                p_index = (data1[i][0], data1[j][0])
            i += 1
        elif temp_sum > sn:
            j -= 1
        else:
            return (data1[i][0],data1[j][0])

    return p_index

if __name__ == '__main__':
    p = [1, 10, 25, 35, 60,55,23,45,78,30]
    r = pick_points(p, 50)
    print(p[r[0]], p[r[1]])
    print(r)
