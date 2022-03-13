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
        curr_new = dummy
        curr_old = head
        node_map = {}
        while curr_old:
            curr_new.next = node_map.get(curr_old, new_node:=Node(x=curr_old.val))
            if curr_old not in node_map:
                node_map[curr_old] = new_node
            curr_new = curr_new.next
            if curr_old.random:
                curr_new.random = node_map.get(curr_old.random, rand_node:=Node(x=curr_old.random.val))
                if curr_old.random not in node_map:
                    node_map[curr_old.random] = rand_node
            curr_old = curr_old.next
        return dummy.next
