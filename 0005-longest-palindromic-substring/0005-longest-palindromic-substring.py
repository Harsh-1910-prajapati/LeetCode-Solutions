class Solution(object):
    def longestPalindrome(self, s):
        st = 0
        end = 0

        for i in range(len(s)):
            len1 = ex(s, i, i)
            len2 = ex(s, i, i+1)
            length = max(len1, len2)
            if length > end - st:
                st = i - (length - 1) // 2
                end = i + length // 2
        return s[st:end+1]
def ex(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right] :
        left -= 1
        right += 1
    return right - left - 1

        