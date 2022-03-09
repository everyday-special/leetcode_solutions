# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(val=-1000)
        curr = dummy
        temp = head
        head = head.next
        while head:
            if temp.val != head.val:
                curr.next = temp
                curr = curr.next
            else:
                while head and head.val == temp.val:
                    head = head.next
            temp = head
            if head:
                head = head.next
        curr.next = temp
        return dummy.next
