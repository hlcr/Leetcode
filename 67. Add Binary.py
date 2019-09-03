class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0 and len(b) == 0:
            return "0"
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        sub = len(a) - len(b)
        if sub > 0:
            b = '0' * sub + b
        elif sub < 0:
            a = '0' * -sub + a

        signal = False
        result = ""
        k = len(a)-1
        while k >= 0:
            i, j = a[k], b[k]
            temp = ord(i) + ord(j) - 96

            if signal:
                temp += 1
            if temp >= 2:
                signal = True
            else:
                signal = False

            result = str(temp % 2) + result
            # print(temp, result)
            k -= 1

        if signal:
            return "1" + result
        return result

if __name__ == '__main__':
    r = Solution().addBinary("11111","111")
    print(r)