class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        copies = {}

        def dfs(cur):
            if cur in copies:
                return copies[cur]

            copy = Node(cur.val)
            copies[cur] = copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)