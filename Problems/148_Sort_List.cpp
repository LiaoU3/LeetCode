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
    ListNode* sortList(ListNode* head) {
        if(!head || !head->next)
            return head;
        ListNode* middle = getMiddle(head);
        ListNode* left = sortList(head);
        ListNode* right = sortList(middle);
        return merge(left, right);
    }
    
    ListNode* merge(ListNode* head1, ListNode* head2){
        // dummy head
        ListNode* res = new ListNode(0);
        ListNode* curr = res;
        while(head1 && head2){
            if(head1->val<head2->val){
                curr->next = head1;
                head1 = head1->next;
            }else{
                curr->next = head2;
                head2 = head2->next;
            }
            curr = curr->next;
        }
        if(!head1) curr->next = head2;
        else curr->next = head1;
        return res->next;
    }
    
    ListNode* getMiddle(ListNode* head){
        ListNode* slow = NULL;
        ListNode* fast = head;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow==NULL ? head :slow->next;
        }
        ListNode* middle = slow->next;
        slow->next = NULL;
        return middle;
    }
};