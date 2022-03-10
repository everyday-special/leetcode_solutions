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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode();
        ListNode *curr = dummy;
        int carry = 0;
        int val;
        while (l1 && l2) {
            val = (l1->val + l2->val + carry) % 10;
            carry = (l1->val + l2->val + carry) / 10;
            curr->next = new ListNode(val=val);
            curr = curr->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        while (l1) {
            val = (l1->val + carry) % 10;
            carry = (l1->val + carry) / 10;
            curr->next = new ListNode(val=val);
            curr = curr->next;
            l1 = l1->next;
        }
        while (l2) {
            val = (l2->val + carry) % 10;
            carry = (l2->val + carry) / 10;
            curr->next = new ListNode(val=val);
            curr = curr->next;
            l2 = l2->next;
        }
        if (carry)
            curr->next = new ListNode(val=carry);
        return dummy->next;
    }
};
