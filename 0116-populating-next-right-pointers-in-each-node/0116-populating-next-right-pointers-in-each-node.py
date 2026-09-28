class Solution:
    def connect(self, root):
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            cur = leftmost

            while cur:
                cur.left.next = cur.right

                if cur.next:
                    cur.right.next = cur.next.left

                cur = cur.next

            leftmost = leftmost.left

        return root