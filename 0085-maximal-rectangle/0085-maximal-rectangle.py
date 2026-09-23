class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        n = len(matrix[0])
        heights = [0] * n
        ans = 0
        
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            
            stack = []
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    ans = max(ans, height * (i - left - 1))
                stack.append(i)
        
        return ans