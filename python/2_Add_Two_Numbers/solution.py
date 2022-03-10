# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 and l2:
            val, carry = (l1.val + l2.val + carry) % 10, (l1.val + l2.val + carry) // 10
            curr.next = ListNode(val=val)
            curr, l1, l2 = curr.next, l1.next, l2.next
        while l1:
            val, carry = (l1.val + carry) % 10, (l1.val + carry) // 10
            curr.next = ListNode(val=val)
            curr, l1 = curr.next, l1.next
        while l2:
            val, carry = (l2.val + carry) % 10, (l2.val + carry) // 10
            curr.next = ListNode(val=val)
            curr, l2 = curr.next, l2.next
        if carry:
            curr.next = ListNode(val=carry)
        return dummy.next
