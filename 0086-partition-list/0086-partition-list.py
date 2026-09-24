class Solution:
    def partition(self, head, x):
        a = ListNode(0)
        b = ListNode(0)
        p, q = a, b

        while head:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next

        q.next = None
        p.next = b.next
        return a.next