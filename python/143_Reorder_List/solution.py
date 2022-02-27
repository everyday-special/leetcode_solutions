# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        prev = None
        while slow:
            temp = slow.next
            prev, prev.next = slow, prev
            slow = temp
        dummy = ListNode()
        curr = dummy
        while head and fast:
            curr.next, head = head, head.next
            curr = curr.next
            curr.next, fast = fast, fast.next
            curr = curr.next
        curr.next = None
        return dummy.next
