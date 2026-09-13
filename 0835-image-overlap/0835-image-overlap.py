class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        result = 0

        for r in range(-n + 1, n):
            for c in range(-n + 1, n):
                count = 0

                for i in range(n):
                    for j in range(n):
                        ni = i + r
                        nj = j + c

                        if 0 <= ni < n and 0 <= nj < n:
                            if img1[i][j] == 1 and img2[ni][nj] == 1:
                                count += 1

                result = max(result, count)

        return result