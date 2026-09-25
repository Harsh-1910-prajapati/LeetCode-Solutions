class Solution:
    def recoverTree(self, root):
        stack = []
        cur = root
        prev = None
        first = None
        second = None

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if prev and prev.val > cur.val:
                if not first:
                    first = prev
                second = cur

            prev = cur
            cur = cur.right

        first.val, second.val = second.val, first.val