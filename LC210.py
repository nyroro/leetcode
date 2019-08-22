class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
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
            return []
        ret = []
        while len(que)>0:
            t = que.pop()
            ret.append(t)
            for child in edges.get(t, []):
                degree[child] -= 1
                if degree[child]<=0:
                    que.append(child)
        if sum(degree) > 0:
            return []
        return ret[::-1]
        