
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
    ListNode* middleNode(ListNode* head) {
        ListNode* slow(head);
        ListNode* fast(head);
        
        int count = 0;
        while(fast != nullptr){
            fast = fast->next;
            if(count%2){
                slow = slow->next;
            }
            count += 1;
        }
        return slow;
    }
};