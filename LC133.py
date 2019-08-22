"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        table = {}
        def dfs(node):
            
            new_node = Node()
            new_node.val = node.val
            
            table[id(node)] = new_node
            
            ret_neighbors = []
            for n in node.neighbors:
                if id(n) in table:
                    ret_neighbors.append(table[id(n)])
                else:
                    ret_neighbors.append(dfs(n))
            new_node.neighbors = ret_neighbors
            return node
        return dfs(node)
                    
                    
            
        