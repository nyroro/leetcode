"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        sum_grid = sum([sum(t) for t in grid])
        if sum_grid == len(grid)*len(grid):
            return Node(True, True, None, None, None,None)
        elif sum_grid == 0:
            return Node(False, True, None, None, None, None)
        
        lg = len(grid)/2
        g0 = [t[:lg] for t in grid[:lg]]
        g1 = [t[lg:] for t in grid[:lg]]
        g2 = [t[:lg] for t in grid[lg:]]
        g3 = [t[lg:] for t in grid[lg:]]
        node0 = self.construct(g0)
        node1 = self.construct(g1)
        node2 = self.construct(g2)
        node3 = self.construct(g3)
        return Node(None, False, node0, node1, node2, node3)
        
        