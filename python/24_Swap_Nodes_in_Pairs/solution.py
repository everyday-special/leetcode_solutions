# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        dummy = ListNode(next=head)
        curr = dummy
        while head:
            if count % 2 == 1:
                temp = head
                head = head.next
            else:
                curr.next = head
                head.next, temp.next = temp, head.next
                head = temp.next
                curr = curr.next.next
            count += 1
        return dummy.next
