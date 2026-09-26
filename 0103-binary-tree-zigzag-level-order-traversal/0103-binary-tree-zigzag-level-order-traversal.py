class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ans = []
        q = [root]
        rev = False
        while q:
            level = [node.val for node in q]
            ans.append(level[::-1] if rev else level)
            q = [child for node in q for child in (node.left, node.right) if child]
            rev = not rev
        return ans