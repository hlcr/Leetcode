class Solution:
    def expand(self, S: str) -> List[str]:
        result = []

        def helper(pre_str, rest_str):
            if len(rest_str) == 0:
                result.append(pre_str)
                return

            i = 0
            if "{" == rest_str[i]:
                options = []
                i += 1
                while "}" != rest_str[i]:
                    options.append(rest_str[i])
                    i += 1
                    if rest_str[i] == ',':
                        i += 1
            else:
                options = [rest_str[i]]

            options.sort()
            for option in options:
                helper(pre_str + option, rest_str[i + 1:])

        helper("", S)
        return result