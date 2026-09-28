class Solution:
    def maxProfit(self, prices):
        mn = prices[0]
        ans = 0

        for price in prices:
            mn = min(mn, price)
            ans = max(ans, price - mn)

        return ans