class Solution:
    def isSymmetric(self, root):
        def check(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and check(a.left, b.right) and check(a.right, b.left)
        return check(root, root)