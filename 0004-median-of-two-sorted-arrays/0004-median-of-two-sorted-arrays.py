class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total_l = len(nums1) + len(nums2)
        half_l = total_l // 2

        left = 0
        right = len(nums1)

        while left <= right:
            parti1 = (left + right) // 2
            parti2 = half_l - parti1

            max_l1 = float('-inf') if parti1 == 0 else nums1[parti1 - 1]
            min_r1 = float('inf') if parti1 == len(nums1) else nums1[parti1]

            max_l2 = float('-inf') if parti2 == 0 else nums2[parti2 - 1]
            min_r2 = float('inf') if parti2 == len(nums2) else nums2[parti2]

            if max_l1 <= min_r2 and max_l2 <= min_r1:

                if total_l % 2 == 0:
                    return (max(max_l1, max_l2) + min(min_r1, min_r2)) / 2.0
                else:
                    return min(min_r1, min_r2)

            elif max_l1 > min_r2:
                right = parti1 - 1

            else:
                left = parti1 + 1