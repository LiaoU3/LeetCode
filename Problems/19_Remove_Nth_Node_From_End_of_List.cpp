// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
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