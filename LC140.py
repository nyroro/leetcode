class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.wordDict = wordDict
        self.memo = {}
        return self.dfs(s)
        
        
    def dfs(self, s):
        if s=='':
            return ['']
        if len(s) in self.memo:
            return self.memo[len(s)]
        ret = []
        for word in self.wordDict:
            if s[0:len(word)] == word:
                for sentence in self.dfs(s[len(word):]):
                    if sentence:
                        result = word+' '+sentence
                    else:
                        result = word
                    ret.append(result)
        self.memo[len(s)] = ret
        return ret
            