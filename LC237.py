# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node!=None:
            node_next = node.next
            if node_next != None:
                node.val = node_next.val
                if node_next.next == None:
                    node.next = None
                    return
            node = node_next