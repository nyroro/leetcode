# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        arr = []
        for i, t in enumerate(lists):
            if t!=None:
                arr.append((t.val, t))
                lists[i] = t.next
        heapq.heapify(arr)
        head = None
        now = head
        while(len(arr)>0):
            
            tmp = heapq.heappop(arr)
            if head==None:
                head = tmp[1]
                now = head
            else:
                now.next = tmp[1]
                now = tmp[1]
            node = tmp[1].next
            if node!=None:
                heapq.heappush(arr,(node.val,node))
        return head
        
                
        