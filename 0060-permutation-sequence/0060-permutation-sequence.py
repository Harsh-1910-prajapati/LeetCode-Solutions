class Solution:
    def getPermutation(self, n, k):
        from math import factorial
        nums = list(range(1, n+1))
        k -= 1
        result = []
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            idx = k // f
            result.append(str(nums.pop(idx)))
            k %= f
        return ''.join(result)