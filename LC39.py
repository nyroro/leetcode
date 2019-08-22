import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        ret = []
        tmp = []
        def dfs(x, y):
            if y == 0:
                ret.append(copy.copy(tmp))
                return
            if x==0:
                return
            
            now = x-1
            t = y
            ori_len = len(tmp)
            
            while t >= 0:
                dfs(x-1, t)
                t -= candidates[now]
                tmp.append(candidates[now])
            del tmp[ori_len:]
            
        dfs(len(candidates), target)
        return ret
        
        