class Solution:
    def reorderList(self, head):
        a = []
        while head:
            a.append(head)
            head = head.next
        i, j = 0, len(a) - 1
        while i < j:
            a[i].next = a[j]
            i += 1
            if i == j:
                break
            a[j].next = a[i]
            j -= 1
        a[i].next = None