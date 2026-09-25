class Solution:
    def inorderTraversal(self, root):
        ans = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right

        return ans