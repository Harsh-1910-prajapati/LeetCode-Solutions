class Solution(object):
    def maxSubArray(self, nums):
        current = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            result = max(result, current)

        return result