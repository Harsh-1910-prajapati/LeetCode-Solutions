class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        def comb(a, b):
            result = 1

            for i in range(1, b + 1):
                result = result * (a - b + i) // i

            return result % MOD

        return comb(n + k - 1, 2 * k)