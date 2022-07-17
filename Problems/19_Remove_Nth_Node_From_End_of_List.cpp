// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // dummyHead
        ListNode* ans = new ListNode(0);
        ans->next = head;
        ListNode* slow = ans;
        ListNode* fast = ans;
        for(int i=0; i<n; i++){
            fast = fast->next;
        }
        cout<<fast->val;
        while(fast->next!=NULL){
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        return ans->next;
    }
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* slow_pre = head;
        while(fast != nullptr){
            if(n <= 0){
                slow_pre = slow;
                slow = slow->next;
            }
            fast = fast->next;
            n--;
        }
        slow_pre->next = slow->next;
        if(n==0){
            return head->next;
        }
        if(slow_pre==slow){
            return nullptr;
        }
        return head;
    }
};