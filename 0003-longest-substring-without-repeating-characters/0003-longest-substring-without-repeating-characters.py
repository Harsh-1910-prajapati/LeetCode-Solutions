class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char = {}
        max_l = 0 
        st = 0 
        for end in range(len(s)):
            if s[end] in char:
                st = max(st, char[s[end]]+1)
            char[s[end]] = end
            max_l = max(max_l, end - st +1)
        return max_l
        