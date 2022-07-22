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
    ListNode* partition(ListNode* head, int x) {
        if(!head || !head->next)
            return head;
        // dummy head
        ListNode* leftStart = new ListNode(0);
        leftStart->next = head;
        ListNode* leftEnd = leftStart;
        ListNode* rightStart = new ListNode(0);
        ListNode* rightEnd = rightStart;
        while(head){
            if(head->val<x){
                leftEnd->next = head;
                leftEnd = leftEnd->next;
            }else{
                rightEnd->next = head;
                rightEnd = rightEnd->next;
            }
            head = head->next;
        }
        rightEnd->next = nullptr;
        leftEnd->next = rightStart->next;
        return leftStart->next;
    }
};