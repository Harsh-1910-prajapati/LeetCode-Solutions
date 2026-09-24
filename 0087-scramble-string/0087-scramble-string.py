class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def solve(a, b):
            key = (a, b)

            if key in memo:
                return memo[key]

            if a == b:
                return True

            if sorted(a) != sorted(b):
                memo[key] = False
                return False

            n = len(a)

            for i in range(1, n):
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    memo[key] = True
                    return True

                if solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i]):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return solve(s1, s2)