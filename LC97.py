class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1=="":
            return s2==s3
        if s2=="":
            return s1==s3
        if len(s1)+len(s2)!=len(s3):
            return False
        dp = [[False]*(len(s2)+1) for i in xrange(len(s1)+1)]
        dp[0][0] = True
        for i in xrange(len(s3)):
            now_length = i+1
            i1 = 0
            i2 = now_length-i1
            if i2>len(s2):
                i2 = len(s2)
                i1 = now_length - i2
            flag = False
            while 0<=i1<=len(s1) and 0<=i2<=len(s2):
                if i1>0 and s1[i1-1] == s3[i]:
                    dp[i1][i2] |= dp[i1-1][i2]
                if i2>0 and s2[i2-1] == s3[i]:
                    dp[i1][i2] |= dp[i1][i2-1]
                
                flag |= dp[i1][i2]
                # print i1, i2, dp[i1][i2]
                i1+=1
                i2-=1
            # print i, flag
        return dp[len(s1)][len(s2)]