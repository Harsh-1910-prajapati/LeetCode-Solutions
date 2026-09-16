class Solution(object):
    def canJump(self, nums):
        reach = 0

        for i in range(len(nums)):
            if i > reach:
                return False

            reach = max(reach, i + nums[i])

            if reach >= len(nums) - 1:
                return True

        return True