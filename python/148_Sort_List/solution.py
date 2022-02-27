# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        temp = []
        while head:
            temp.append(head)
            head = head.next
        temp.sort(key=lambda x: x.val)
        head, curr = temp[0], temp[0]
        for i in range(1, len(temp)):
            curr.next = temp[i]
            curr = curr.next
        curr.next = None
        return head
