def get_most_word(text, ewl):
    text = text.lower()
    text1 = ""
    word_list = []
    for c in text:
        if c.isalpha():
            text1 += c
        elif text1:
            word_list.append(text1)
            text1 = ""

    rd = dict()
    max_num = 0
    result_list = []
    for word in word_list:
        rd[word] = rd.get(word, 0) + 1
    print(rd)

    for k, v in rd.items():
        if max_num < v:
            result_list = [k]
            max_num = v
        elif max_num == v:
            result_list.append(k)

    return result_list


if __name__ == '__main__':
    ewl = []
    r = get_most_word("The imported definitions imported may be significantly out of date, and any more recent senses may be completely missing. (See the entry for rese in Webster's Revised ...", ewl)
    print(r)


