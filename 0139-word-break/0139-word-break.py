class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for w in wordDict:
                if i >= len(w) and dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = True
                    break
        return dp[-1]