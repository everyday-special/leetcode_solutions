# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 0
        tail, curr = None, head
        while curr:
            length += 1
            tail, curr = curr, curr.next
        tail.next = head
        for _ in range(0, length - k % length):
            tail, head = head, head.next
        tail.next = None
        return head
