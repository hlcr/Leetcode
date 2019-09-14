def find_distinct(string, k):
    if len(string) < k:
        return []

    char_set = set()
    char_queue = []
    result = []
    for i in range(len(string)):
        if string[i] in char_set:
            temp = ''
            while char_queue and temp != string[i]:
                temp = char_queue.pop(0)
                char_set.remove(temp)
        char_queue.append(string[i])
        char_set.add(string[i])

        if len(char_queue) == k:
            result.append(''.join(char_queue))
            char_set.remove(char_queue.pop(0))

    return result

if __name__ == '__main__':
    r = find_distinct("awaglknagawunagwkwagl", 4)
    print(r)
