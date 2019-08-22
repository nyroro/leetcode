class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        table = {')':'(', "}":"{",']':'['}
        for t in list(s):
            if t in '({[':
                stack.append(t)
            else:
                if len(stack) > 0 and stack[-1] == table.get(t):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                    
        