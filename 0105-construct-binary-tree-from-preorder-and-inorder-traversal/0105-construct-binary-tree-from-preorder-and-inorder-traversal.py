class Solution:
    def buildTree(self, preorder, inorder):
        pos = {v: i for i, v in enumerate(inorder)}
        idx = [0]

        def build(l, r):
            if l > r:
                return None

            val = preorder[idx[0]]
            idx[0] += 1

            root = TreeNode(val)
            m = pos[val]

            root.left = build(l, m - 1)
            root.right = build(m + 1, r)

            return root

        return build(0, len(inorder) - 1)