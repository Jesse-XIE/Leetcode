// Description: 
// ---------------

// Given a list, rotate the list to the right by k places, where k is non-negative.
// For example:
// Given 1->2->3->4->5->NULL and k = 2,
// return 4->5->1->2->3->NULL.



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head != NULL){
            ListNode *node1 = head;
            int len = 1;
            while(node1->next != NULL){
                node1 = node1->next;
                ++len;
            }
            node1->next = head;
            int shift = len - k % len;
            for(int i = 0; i != shift; ++i){
                node1 = node1->next;
            }
            head = node1->next;
            node1->next = NULL;
        }
        return head;
    }
};