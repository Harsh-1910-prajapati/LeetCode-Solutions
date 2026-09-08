class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        cl = float('inf')

        for i in range(len(nums) - 2):
            li = i + 1
            ri = len(nums) - 1

            while li < ri:
                t = nums[i] + nums[li] + nums[ri]

                if t == target:
                    return t

                if abs(t - target) < abs(cl - target):
                    cl = t

                if t < target:
                    li += 1
                else:
                    ri -= 1

        return cl
        