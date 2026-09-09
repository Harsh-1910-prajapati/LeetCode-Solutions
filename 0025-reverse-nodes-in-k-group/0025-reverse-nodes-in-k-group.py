class Solution(object):
    def reverseKGroup(self, head, k):
        current = head
        count = 0

        while current and count < k:
            current = current.next
            count += 1

        if count < k:
            return head

        current = head
        prev = None

        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        head.next = self.reverseKGroup(current, k)

        return prev