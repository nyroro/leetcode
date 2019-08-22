# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        if head.next == None:
            return True
        p = head.next
        q = head
        mid_start = q.next
        
        while p != None:
            p = p.next
            q = q.next
            if p != None:
                p = p.next
                mid_start = q.next
            else:
                mid_start = q
        mid_end = q
        p = head
        q = head.next
        p.next = mid_end
        while q != mid_end:
            r = q.next
            q.next = p
            p = q
            q = r
            
        head = p
        
        while head!=mid_end:
            if head.val!=mid_start.val:
                return False
            head = head.next
            mid_start = mid_start.next
        return True
        
        