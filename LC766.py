"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def flatten(head):
            p = head
            if p==None:
                return head, p
            q = p.next
            while q!= None:
                if p.child != None:
                    chead, cend = flatten(p.child)
                    p.next = chead
                    chead.prev = p
                    cend.next = q
                    q.prev = cend
                    p.child = None
                
                p = q
                q = p.next
            if p.child!=None:
                chead,cend= flatten(p.child)
                p.next = chead
                chead.prev = p
                p.child = None
                p = cend
            return head,p
        head,end = flatten(head)
        return head
                
        