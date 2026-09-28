class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        ans = 0

        for n in s:
            if n - 1 not in s:
                cur = n
                length = 1

                while cur + 1 in s:
                    cur += 1
                    length += 1

                ans = max(ans, length)

        return ans