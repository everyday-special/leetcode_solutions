/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head)
            return head;
        int len = 0;
        ListNode * tail = nullptr;
        ListNode * curr = head;
        while (curr) {
            len++;
            tail = curr;
            curr = curr->next;
        }
        k = k % len;
        int count = len - k;
        tail->next = head;
        ListNode * prev = tail;
        while (count > 0) {
            count -= 1;
            prev = head;
            head = head->next;
        }
        prev->next = nullptr;
        return head;
    }
};
