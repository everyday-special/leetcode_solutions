# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            if l1:
                return l1
            elif l2:
                return l2
            else:
                return None
        if l1.val <= l2.val:
            nxt = l1.next
            l1.next = self.mergeTwoLists(nxt, l2)
            return l1
        else:
            nxt = l2.next
            l2.next = self.mergeTwoLists(l1, nxt)
            return l2
