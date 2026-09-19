from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        a = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        n = len(a)
        starts = [x[0] for x in a]

        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, a[i][1])

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, idx = a[i]

            for k in range(1, 5):
                skip = dp[i + 1][k]

                take_w = w + dp[nxt[i]][k - 1][0]
                take_ids = tuple(sorted((idx,) + dp[nxt[i]][k - 1][1]))

                if take_w > skip[0]:
                    dp[i][k] = (take_w, take_ids)
                elif take_w < skip[0]:
                    dp[i][k] = skip
                else:
                    dp[i][k] = min(
                        (take_w, take_ids),
                        skip,
                        key=lambda x: x[1]
                    )

        return list(dp[0][4][1])