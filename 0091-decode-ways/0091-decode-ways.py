class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        a, b = 1, 1

        for i in range(1, len(s)):
            c = 0

            if s[i] != '0':
                c += b

            if 10 <= int(s[i - 1:i + 1]) <= 26:
                c += a

            a, b = b, c

        return b