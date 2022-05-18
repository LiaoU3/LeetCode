#include <stdio.h>
#include <stdlib.h>
// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* pre  = NULL;
    struct ListNode* curr = head;
    struct ListNode* nxt;
    while(curr){
        nxt = curr -> next;
        curr -> next = pre;
        pre = curr;
        curr = nxt;
    }
    return pre;
}