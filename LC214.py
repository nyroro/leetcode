class Solution(object):
    def get_next(self, s):
        next = [-1] * len(s)
        j = 0
        k = -1
        while j < len(s)-1:
            if k == -1 or s[j] == s[k]:
                j+=1
                k+=1
                next[j] = k
            else:
                k = next[k]
        return next
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        next = self.get_next(s+'#'+s[::-1])
        
        return s[::-1][:len(s)-next[-1]-1]+s