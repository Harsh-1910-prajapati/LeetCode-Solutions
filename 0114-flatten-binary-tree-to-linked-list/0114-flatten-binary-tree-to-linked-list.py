class Solution:
    def flatten(self, root):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        right = root.right
        root.right = root.left
        root.left = None

        cur = root
        while cur.right:
            cur = cur.right

        cur.right = right