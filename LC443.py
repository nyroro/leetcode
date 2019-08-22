class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        now = chars[0]
        cnt = 1
        
        tmpIndex = 0
        for i in xrange(1, len(chars)):
            if chars[i] == chars[i-1]:
                cnt+=1
            else:
                chars[tmpIndex] = now
                tmpIndex += 1 
                if cnt > 1:
                    for c in str(cnt):
                        chars[tmpIndex] = c
                        tmpIndex += 1
                now = chars[i]
                cnt = 1
        chars[tmpIndex] = now
        tmpIndex += 1 
        if cnt > 1:
            for c in str(cnt):
                chars[tmpIndex] = c
                tmpIndex += 1
        return tmpIndex
                    
                
        