class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                dummy = ListNode(0)
                current = dummy

                while l1 and l2:
                    if l1.val <= l2.val:
                        current.next = l1
                        l1 = l1.next
                    else:
                        current.next = l2
                        l2 = l2.next

                    current = current.next

                current.next = l1 or l2
                merged.append(dummy.next)

            lists = merged

        return lists[0]