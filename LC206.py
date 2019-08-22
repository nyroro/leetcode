# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p = head
        if p.next == None:
            return p
        q = p.next
        p.next = None
        
        while q != None:
            r = q.next
            q.next = p
            p = q
            q = r
        return p