import collections
from functools import reduce

def minimumLengthEncoding(words):
    words = list(set(words))  # remove duplicates
    words = list(set(words))  # remove duplicates
    # Trie is a nested dictionary with nodes created
    # when fetched entries are missing
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()

    # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
    nodes = [reduce(dict.__getitem__, word[::-1], trie)
             for word in words]

    # return nodes

    # print(reduce(dict.__getitem__, 'abbbcd', trie))

    for i, word in enumerate(words):
        print(nodes[i])
        # print(word[::-1])

    # Add word to the answer if it's node has no neighbors
    return sum(len(word) + 1
               for i, word in enumerate(words)
               if len(nodes[i]) == 0)


if __name__ == '__main__':
    n = minimumLengthEncoding(['time', 'me', 'fish'])
    # d = dict()
    # d['b'] = 1
    # print((dict.__getitem__(d, 'b')))