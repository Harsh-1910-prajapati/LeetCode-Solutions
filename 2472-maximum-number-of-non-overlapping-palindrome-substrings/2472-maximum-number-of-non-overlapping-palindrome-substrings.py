class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]

            if i + k <= n and s[i:i + k] == s[i:i + k][::-1]:
                dp[i] = max(dp[i], 1 + dp[i + k])

            if i + k + 1 <= n and s[i:i + k + 1] == s[i:i + k + 1][::-1]:
                dp[i] = max(dp[i], 1 + dp[i + k + 1])

        return dp[0]