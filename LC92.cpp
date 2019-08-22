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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if(m==n)
        {
            return head;
        }
        ListNode *p = head;
        ListNode *pre = NULL;
        m--;
        n--;
        for(int i=0;i<m;i++)
        {
            pre = p;
            p = p->next;
        }
        ListNode *q=p;
        for(int i=m;i<n;i++)
        {
            q=q->next;
        }
        ListNode *r_start = reverse(p, q);
        if(pre)
        {
            pre->next=r_start;
            return head;
        }
        else
        {
            return r_start;
        }
    }
    
    ListNode* reverse(ListNode *start, ListNode *end)
    {
        ListNode *p, *q, *r;
        p = start;
        q = start->next;
        if(q==end)
        {
            p->next = q->next;
            q->next = p;
            return q;
        }
        r = q->next;
        start->next = end->next;
        q->next = p;
        while(r!=end)
        {
            p = q;
            q = r;
            r = r->next;
            q->next = p;
        }
        
        r->next = q;
        return end;
    }
};