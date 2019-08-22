class Solution(object):
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        edges = {}
        degree = [0]*numCourses
        # 建边
        for a,b in prerequisites:
            edges.setdefault(a, []).append(b)
            degree[b] += 1
        que = []
        for i in xrange(numCourses):
            if degree[i] == 0:
                que.append(i)
        if len(que) == 0:
            return False
        while len(que)>0:
            t = que.pop()
            for child in edges.get(t, []):
                degree[child] -= 1
                if degree[child]<=0:
                    que.append(child)
        
        return sum(degree)<=0
        
        