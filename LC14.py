class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ''
        if len(strs) == 0:
            return ''
        
        ret = strs[0]
        
        for i in range(1, len(strs)):
            now = strs[i]
            j = 0
            while j<len(now) and j<len(ret) and now[j] == ret[j]:
                j+=1
            ret = ret[:j]
            if len(ret) == 0:
                break
        return ret
        