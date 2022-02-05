# Inspired by checking discussion and learning about heapq module

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(-1)
        curr = dummy
        count = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, count, l))
                count += 1
        while heap:
            nxt = heapq.heappop(heap)
            curr.next = nxt[2]
            curr = curr.next
            if nxt[2].next:
                heapq.heappush(heap, (nxt[2].next.val, count, nxt[2].next))
                count += 1
        return dummy.next

