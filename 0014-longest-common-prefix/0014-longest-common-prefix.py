class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        min_l = min(len(s) for s in strs)

        com_pre = ""
        for i in range(min_l):
            curr_c = strs[0][i]
            if all(s[i] == curr_c for s in strs):
                com_pre += curr_c
            else:
                break
        return com_pre
