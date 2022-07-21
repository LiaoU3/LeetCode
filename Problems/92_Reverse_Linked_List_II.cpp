// #include<stddef.h>
#include<iostream>

using namespace std;
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* ans = new ListNode(0);
        ans->next = head;
        ListNode* curr = ans;
        ListNode* leftEnd;
        ListNode* rightStart = nullptr;

        for(int i=0; i<left-1; i++){
            curr = curr->next;
        }
        leftEnd = curr;
        curr = curr->next;
        ListNode* middleEnd = curr;
        ListNode* pre = nullptr;
        ListNode* middleStart;
        for(int i=left; i<=right; i++){
            ListNode* nxt = curr->next;
            curr->next = pre;
            pre = curr;
            middleStart = pre;
            curr = nxt;
        }
        leftEnd->next = middleStart;
        middleEnd->next = curr;
        return ans->next;
    }
};