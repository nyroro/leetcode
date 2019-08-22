from collections import deque
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d1 = deque()
        self.d2 = deque()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.d2.append(x)
        
    def move(self):
        while len(self.d2) > 0:
            self.d1.append(self.d2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.d1) == 0:
            self.move()
        return self.d1.pop()
        
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.d1) == 0:
            self.move()
        return self.d1[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.d1) == 0 and len(self.d2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()