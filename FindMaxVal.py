def find_max_val(array):
    left, right = 0, len(array)-1
    max_result = -9999
    result = []
    while left <= right:
        current_result = array[left] + array[right] + right - left
        if max_result < current_result:
            result = [left, right]
            max_result = current_result

        if array[left] < array[right]:
            left += 1
        else:
            right -= 1
    return result


if __name__ == '__main__':
    a = [6, 2, 7, 4, 4, 1, 6]
    r = find_max_val(a)
    print(r)
