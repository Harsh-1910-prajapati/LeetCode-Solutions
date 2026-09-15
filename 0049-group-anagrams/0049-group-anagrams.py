class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for s in strs:
            key = [0] * 26

            for ch in s:
                key[ord(ch) - ord('a')] += 1

            key = tuple(key)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())