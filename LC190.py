class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # print n
        t = 0
        cnt = 0
        while n>0:
            # print n%2,
            t=t*2+n%2
            n/=2
            cnt+=1
        while cnt<32:
            t=t*2
            cnt+=1
            
        return t