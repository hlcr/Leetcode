import re
class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        pattern = re.compile('[aeiouAEIOU]')
        return pattern.sub('', S)

if __name__ == '__main__':
    r = Solution().removeVowels("leetcodeisacommunityforcoders")
    print(r)