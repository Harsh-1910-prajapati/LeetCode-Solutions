class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        tree = [(1 % k, [0] * k) for _ in range(2 * size)]

        for i in range(n):
            v = nums[i] % k
            cnt = [0] * k
            cnt[v] = 1
            tree[size + i] = (v, cnt)

        def merge(a, b):
            p1, c1 = a
            p2, c2 = b

            p = (p1 * p2) % k
            c = c1[:]

            for r in range(k):
                c[(p1 * r) % k] += c2[r]

            return p, c

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        def update(pos, val):
            i = size + pos
            v = val % k
            cnt = [0] * k
            cnt[v] = 1
            tree[i] = (v, cnt)

            i //= 2
            while i:
                tree[i] = merge(tree[i * 2], tree[i * 2 + 1])
                i //= 2

        def query(l, r):
            left = None
            right = None

            l += size
            r += size + 1

            while l < r:
                if l & 1:
                    left = tree[l] if left is None else merge(left, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right = tree[r] if right is None else merge(tree[r], right)

                l //= 2
                r //= 2

            if left is None:
                return right
            if right is None:
                return left
            return merge(left, right)

        ans = []

        for idx, val, start, x in queries:
            update(idx, val)
            ans.append(query(start, n - 1)[1][x])

        return ans