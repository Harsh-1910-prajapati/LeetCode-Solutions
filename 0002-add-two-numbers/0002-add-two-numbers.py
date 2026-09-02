class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dumm = ListNode(0)
        curr = dumm
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, sum_v = divmod(val1 + val2 + carry, 10)

            curr.next = ListNode(sum_v)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dumm.next