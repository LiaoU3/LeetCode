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
	if(l1==NULL) return l2;
	if(l2==NULL) return l1;
    ListNode* ans = new ListNode(0);
    ListNode* curr = ans;
    int carry = 0;
    while(l1!=NULL || l2!=NULL || carry){
        int val1 = l1 ? l1->val : 0;
        int val2 = l2 ? l2->val : 0;
        int num = val1+val2+carry;
        carry = num/10;
        num %= 10;
        ListNode* node = new ListNode(num);
        curr->next = node;
        curr = curr->next;
        if(l1!=NULL) l1 = l1->next;
        if(l2!=NULL) l2 = l2->next;
    }
    return ans->next;
}

};