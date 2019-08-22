# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        if p==None:
            return head
        q = head.next
        if q==None:
            return p
        head = q
        q = q.next
        head.next = p
        p.next = q
        
        while p.next != None:
            q = p.next
            if q.next == None:
                break
            r = q.next
            p.next = r
            r = r.next
            p.next.next = q
            q.next = r
            p = q
        return head
            
        
        
        