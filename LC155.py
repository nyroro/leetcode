class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.second = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack)==0:
            self.second.append(x)
        else:
            self.second.append(min(x, self.second[-1]))
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(-1)
        self.second.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.second[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()