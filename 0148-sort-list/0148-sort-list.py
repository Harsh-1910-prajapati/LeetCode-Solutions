class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        a = []
        while head:
            a.append(head.val)
            head = head.next
        a.sort()
        head = ListNode(a[0])
        cur = head
        for x in a[1:]:
            cur.next = ListNode(x)
            cur = cur.next
        return head