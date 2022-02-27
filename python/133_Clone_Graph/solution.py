# Written after checking discussion

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        if not root:
            return None
        node_map = {}
        q = deque([root])
        node_map[root] = Node(root.val)
        while len(q) > 0:
            curr = q.popleft()
            for adj_node in curr.neighbors:
                if adj_node not in node_map:
                    q.append(adj_node)
                    node_map[adj_node] = Node(val=adj_node.val)
                node_map[curr].neighbors.append(node_map[adj_node])
        return node_map[root]
