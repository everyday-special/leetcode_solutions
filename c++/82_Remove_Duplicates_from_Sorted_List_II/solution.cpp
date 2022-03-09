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
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head)
            return head;
        ListNode * dummy = new ListNode(-1000);
        ListNode * curr = dummy;
        ListNode * temp = head;
        head = head->next;
        while (head) {
            if (temp->val != head->val) {
                curr->next = temp;
                curr = curr->next;
            }
            else {
                while (head && head->val == temp->val) {
                    head = head->next;
                }
            }
            temp = head;
            if (head)
                head = head->next;
        }
        curr->next = temp;
        return dummy->next;
    }
};
