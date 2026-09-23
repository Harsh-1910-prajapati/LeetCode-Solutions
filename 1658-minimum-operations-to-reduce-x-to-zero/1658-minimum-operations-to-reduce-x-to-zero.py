class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x
        
        if target < 0:
            return -1
        
        if target == 0:
            return len(nums)
        
        left = 0
        curr = 0
        longest = -1
        
        for right in range(len(nums)):
            curr += nums[right]
            
            while curr > target and left <= right:
                curr -= nums[left]
                left += 1
            
            if curr == target:
                longest = max(longest, right - left + 1)
        
        return -1 if longest == -1 else len(nums) - longest
        