class Solution:
    def copyRandomList(self, head):
        d = {}
        cur = head
        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            d[cur].next = d.get(cur.next)
            d[cur].random = d.get(cur.random)
            cur = cur.next
        return d.get(head)