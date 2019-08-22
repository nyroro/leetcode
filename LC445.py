# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = 0
        b = 0
        while l1:
            a = a*10+l1.val
            l1 = l1.next
        while l2:
            b = b*10+l2.val
            l2 = l2.next
        c = a+b
        c = str(c)
        head = ListNode(int(c[0]))
        p = head
        
        for i in xrange(1,len(c)):
            q = ListNode(int(c[i]))
            p.next = q
            p = q
        return head
        