class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1]*len(ratings)
        for i in xrange(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i]=candy[i-1]+1
        for i in xrange(len(ratings)-1, 0,-1):
            if ratings[i] < ratings[i-1]:
                candy[i-1] = max(candy[i-1], candy[i]+1)
        print candy
        return sum(candy)
                    
                    
        