class Solution:
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        return len(s) - s.rfind(' ') - 1