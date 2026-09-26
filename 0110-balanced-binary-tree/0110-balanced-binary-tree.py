class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            l = height(node.left)
            if l == -1:
                return -1
            r = height(node.right)
            if r == -1 or abs(l - r) > 1:
                return -1
            return 1 + max(l, r)

        return height(root) != -1