class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')
        best = [INF] * n  # best[i] = min length of a valid subarray ending at or before i
        left = 0
        curr_sum = 0
        result = INF
        min_len_so_far = INF

        for right in range(n):
            curr_sum += arr[right]
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                curr_len = right - left + 1
                if left > 0 and best[left - 1] != INF:
                    result = min(result, best[left - 1] + curr_len)
                min_len_so_far = min(min_len_so_far, curr_len)

            best[right] = min_len_so_far

        return result if result != INF else -1