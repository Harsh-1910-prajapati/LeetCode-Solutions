class Solution:
    def reverseDegree(self, s):
        ans = 0

        for i, c in enumerate(s, 1):
            value = 26 - (ord(c) - ord('a'))
            ans += i * value

        return ans