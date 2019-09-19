
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for t in strs:
            ret.setdefault(str(sorted(t)), []).append(t)
            
        return ret.values()
        
        