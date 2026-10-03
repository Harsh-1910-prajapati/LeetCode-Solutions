class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        while head:
            cur = head
            head = head.next
            p = dummy
            while p.next and p.next.val < cur.val:
                p = p.next
            cur.next = p.next
            p.next = cur
        return dummy.next