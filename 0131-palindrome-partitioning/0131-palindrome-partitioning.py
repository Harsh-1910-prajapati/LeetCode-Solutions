class Solution:
    def partition(self, s):
        ans = []

        def dfs(start, path):
            if start == len(s):
                ans.append(path[:])
                return

            for end in range(start, len(s)):
                part = s[start:end + 1]

                if part == part[::-1]:
                    path.append(part)
                    dfs(end + 1, path)
                    path.pop()

        dfs(0, [])
        return ans