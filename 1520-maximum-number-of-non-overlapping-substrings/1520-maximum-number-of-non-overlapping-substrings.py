class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - 97
            first[c] = min(first[c], i)
            last[c] = i

        def expand(start):
            end = last[ord(s[start]) - 97]
            i = start

            while i <= end:
                c = ord(s[i]) - 97
                if first[c] < start:
                    return None
                end = max(end, last[c])
                i += 1

            return start, end

        intervals = []

        for i in range(n):
            c = ord(s[i]) - 97
            if first[c] == i:
                x = expand(i)
                if x:
                    intervals.append(x)

        intervals.sort(key=lambda x: x[1])

        ans = []
        prev = -1

        for l, r in intervals:
            if l > prev:
                ans.append(s[l:r + 1])
                prev = r

        return ans