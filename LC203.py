# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        
        while head != None and head.val == val:
            head = head.next
        if head == None:
            return None
        p = head
        while p != None:
            q = p.next
            if q != None:
                if q.val == val:
                    p.next = q.next
                else:
                    p = q
            else:
                p = p.next
        return head
        