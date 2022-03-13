"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        curr_new, curr_old, node_map = dummy, head, {None: None}
        while curr_old:
            if curr_old not in node_map:
                node_map[curr_old] = Node(x=curr_old.val)
            curr_new.next, curr_new = node_map[curr_old], node_map[curr_old]
            if curr_old.random not in node_map:
                node_map[curr_old.random] = Node(x=curr_old.random.val)
            curr_new.random, curr_old = node_map[curr_old.random], curr_old.next
        return dummy.next
