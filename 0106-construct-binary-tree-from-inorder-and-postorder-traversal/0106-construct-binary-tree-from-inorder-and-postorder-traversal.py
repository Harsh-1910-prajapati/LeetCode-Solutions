class Solution:
    def buildTree(self, inorder, postorder):
        pos = {v: i for i, v in enumerate(inorder)}
        idx = [len(postorder) - 1]

        def build(l, r):
            if l > r:
                return None

            val = postorder[idx[0]]
            idx[0] -= 1

            root = TreeNode(val)
            m = pos[val]

            root.right = build(m + 1, r)
            root.left = build(l, m - 1)

            return root

        return build(0, len(inorder) - 1)