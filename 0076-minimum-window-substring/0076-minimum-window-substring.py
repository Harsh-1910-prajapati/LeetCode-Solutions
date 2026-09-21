class Solution(object):
    def minWindow(self, s, t):
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        count = 0
        best = ""
        window = {}

        for right, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] <= need[c]:
                count += 1

            while count == len(t):
                if not best or right - left + 1 < len(best):
                    best = s[left:right + 1]

                x = s[left]
                window[x] -= 1

                if x in need and window[x] < need[x]:
                    count -= 1

                left += 1

        return best