class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        root = TreeNode(slow.val)

        if slow != head:
            root.left = self.sortedListToBST(head)

        root.right = self.sortedListToBST(slow.next)

        return root