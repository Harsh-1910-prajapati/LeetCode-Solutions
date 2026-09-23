class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            if head.next and head.val == head.next.val:
                val = head.val
                while head and head.val == val:
                    head = head.next
                prev.next = head
            else:
                prev = head
                head = head.next
        
        return dummy.next