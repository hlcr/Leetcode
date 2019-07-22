class Solution(object):

    def generate_data_list(self, lt):
        ltr = []
        if int(lt) == 0:
            ltr = [0]
        elif lt[0] == '0':
            ltr = [int(lt) / (10**(len(lt)-1))]
        else:
            for i in range(0, len(lt)):
                if i == 0:
                    ltr.append(int(lt))
                else:
                    ltr.append(int(lt) / (10 ** i))
        return ltr

    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:len(S)-1]
        result = []
        for i in range(1, len(S)):
            lt = S[:i]
            rt = S[i:]

            ltr = self.generate_data_list(lt)
            rtr = self.generate_data_list(rt)

            for l in ltr:
                for r in rtr:
                    result.append("({}, {})".format(l, r))

        return result



def make(frag):
    N = len(frag)
    for d in range(1, N+1):
        left = frag[:d]
        right = frag[d:]
        if ((not left.startswith('0') or left == '0')
                and (not right.endswith('0'))):
            yield left + ('.' if d != N else '') + right

print(Solution().ambiguousCoordinates("(0123)"))
for i in make("1230"):
    print(i)