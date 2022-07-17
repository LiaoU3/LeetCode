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
    bool isPalindrome(ListNode* head) {
        if(!head) return NULL;
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast->next && fast->next->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        ListNode* rev = reverse(slow->next);
        while(rev){
            if(rev->val!=head->val) return false;
            rev = rev->next;
            head = head->next;
        }
        return true;
    }

    ListNode* reverse(ListNode* head){
        ListNode* pre = NULL;
        ListNode* curr = head;
        while(curr){
            ListNode* tmp = curr->next;
            curr->next = pre;
            pre = curr;
            curr = tmp;
        }
        return pre;
    }


};