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
    ListNode* oddEvenList(ListNode* head) {
        if(head==NULL || head->next==NULL||head->next->next==NULL)
        return head;
        ListNode* curr = head->next;
        ListNode* oddEnd = head;
        ListNode* evenEnd = head->next;
        bool isOdd = false;
        while(curr){
            if(isOdd){
                ListNode* nxt = curr->next;
                ListNode* evenStart = oddEnd->next;
                oddEnd->next = curr;
                curr->next = evenStart;
                evenEnd->next = nxt;
                curr = nxt;
                oddEnd = oddEnd->next;
            }else{
                evenEnd = curr;
                curr = curr->next;
            }
            isOdd = !isOdd;
        }       

        return head;
    }

};