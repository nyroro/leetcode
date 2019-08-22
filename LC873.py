# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
import random
class Solution(object):
    def match(self, a, b):
        cnt = 0
        for t in xrange(len(a)):
            if a[t]==b[t]:
                cnt+=1
        return cnt
    
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        t = random.randint(0, len(wordlist)-1)
        cnt = master.guess(wordlist[t])
        if cnt == 6:
            return
        next_words = [tt for tt in wordlist if self.match(wordlist[t], tt)==cnt]
        self.findSecretWord(next_words, master)