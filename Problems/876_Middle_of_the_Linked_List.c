
// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* middleNode(struct ListNode* head){
    struct ListNode* curr = head;
    struct ListNode* middle = head;
    int cnt = -1;
    while (curr){
        curr = curr -> next;
        if (cnt %2 == 0){
            middle = middle -> next;
        }
        cnt += 1;
    }
    return middle;
}