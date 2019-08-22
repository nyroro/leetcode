# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        q = head
        while p != None and q!=None:
            p = p.next
            q = q.next
            if q==None:
                return None
            q = q.next
            if p == q:
                break
        if p!=None and q!=None:
            p = head
            while p!=q:
                p = p.next
                q = q.next
            return p
        return None
        