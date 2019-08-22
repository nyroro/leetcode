# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        a = head
        if a.next == None:
            return a
        b = a.next
        now = b.next
        head = a
        ehead = b
        cnt = 0
        while now != None:
            if cnt%2 == 0:
                a.next = now
                a = a.next
            else:
                b.next = now
                b = b.next
            now = now.next
            cnt += 1
        a.next = ehead
        b.next = None
        return head
            
            