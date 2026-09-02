
class Solution(object):
    def twoSum(self, nums, target):
        num1 = {}

        for i, num in enumerate(nums):
            com = target - num

            if com in num1:
                return [num1[com], i]

            num1[num] = i

        return []
