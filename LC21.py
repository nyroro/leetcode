# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        p = l1
        q = l2
        if p.val<q.val:
            head = p
            p = p.next
        else:
            head = q
            q = q.next
            
        now = head
        while p!=None and q!=None:
            if p.val < q.val:
                now.next = p
                p = p.next
            else:
                now.next = q
                q = q.next
            now = now.next
        if p==None:
            now.next = q
        else:
            now.next = p
        return head
            
        