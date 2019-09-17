class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        if not paragraph:
            return ""
        paragraph = paragraph.lower()
        r_dict = dict()
        max_num = 0
        result = ""
        temp = ""
        for w in paragraph:
            if w.isalpha():
                temp = temp + w
            else:
                if temp in banned:
                    temp = ''
                    continue
                r_dict[temp] = r_dict.get(temp, 0) + 1
                if r_dict[temp] > max_num:
                    result = temp
                    max_num = r_dict[temp]
                temp = ""

        return result

if __name__ == '__main__':
    r = Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    from collections import Counter
    counter = Counter(['1', '2', '1', '2', '3'])
    for k, v in counter.most_common():
        print(k, v)
    print(r)