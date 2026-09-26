class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            ans.append([node.val for node in q])
            q = [child for node in q for child in (node.left, node.right) if child]
        return ans