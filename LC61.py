# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head
        length = 0
        t = head
        while t!=None:
            length += 1
            t = t.next
        k%=length
        if k==0:
            return head
        k = length - k
        t = head
        while k>0:
            t = t.next
            k -= 1
        p = t
        print p
        while p.next!=None:
            p = p.next
        p.next = head
        p = head
        while p.next!=t:
            p=p.next
        p.next = None
        return t