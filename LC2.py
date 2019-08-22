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
        t = 1
        while l1:
            a += t*l1.val
            t*=10
            l1 = l1.next
        b=0
        t=1
        while l2:
            b+=t*l2.val
            t*=10
            l2 = l2.next
        c = a+b
        
        head = ListNode(int(c%10))
        p=head
        c//=10
        while c>0:
            q = ListNode(int(c%10))
            c//=10
            p.next = q
            p = q
        return head
        
        