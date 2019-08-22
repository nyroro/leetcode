import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted([t for t in candidates if t <= target])
        ret = []
        def dfs(index, arr):
            if sum(arr) == target:
                ret.append(copy.copy(arr))
                return
            if sum(arr)>target:
                return
            
            if index == len(candidates):
                return
            arr.append(candidates[index])
            dfs(index+1, arr)
            arr.pop(-1)
            while index+1<len(candidates) and candidates[index+1]==candidates[index]:
                index = index+1
            dfs(index+1, arr)
        dfs(0, [])
        return ret
        