class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        table = {}
        for k, v in people:
            table.setdefault(k,[]).append(v)
        ret = [None]*len(people)
        for k in sorted(table.keys()):
            t = sorted(table[k])
            nowIndex = 0
            while nowIndex<len(ret) and ret[nowIndex]!=None:
                nowIndex+=1
            nowFill = 0
            for t1 in t:
                while nowFill < t1:
                    nowFill+=1
                    nowIndex+=1
                    while nowIndex<len(ret) and ret[nowIndex]!=None:
                        nowIndex+=1
                # print ret
                # print t1, nowIndex
                ret[nowIndex] = (k, t1)
                nowFill+=1
                nowIndex+=1
                while nowIndex<len(ret) and ret[nowIndex]!=None:
                    nowIndex+=1
        
        return ret