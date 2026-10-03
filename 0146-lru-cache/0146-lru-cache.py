class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.c = capacity
        self.d = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev

    def insert(self, n):
        n.prev = self.right.prev
        n.next = self.right
        self.right.prev.next = n
        self.right.prev = n

    def get(self, key):
        if key not in self.d:
            return -1
        n = self.d[key]
        self.remove(n)
        self.insert(n)
        return n.val

    def put(self, key, value):
        if key in self.d:
            self.remove(self.d[key])

        n = Node(key, value)
        self.d[key] = n
        self.insert(n)

        if len(self.d) > self.c:
            n = self.left.next
            self.remove(n)
            del self.d[n.key]