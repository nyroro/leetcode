import heapq
class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.t = {}
        self.rev = {}
        self.min = None
        self.max = None
        
    def insert(self, key):
        val = self.t[key]
        if val not in self.rev:
            self.rev[val] = set()
        self.rev[val].add(key)
        if self.min == None:
            self.min = val
        else:
            self.min = min(self.min, val)
        if self.max == None:
            self.max = val
        else:
            self.max = max(self.max, val)
    
    def delete(self, key):
        val = self.t[key]
        self.rev[val].remove(key)
        if len(self.rev[val])==0:
            self.rev.pop(val)
            if val == self.max:
                self.max = None
            if val == self.min:
                self.min = None

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key not in self.t:
            self.t[key] = 1
        else:
            self.delete(key)
            self.t[key]+=1
        self.insert(key)
        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key not in self.t:
            return
        self.delete(key)
        self.t[key] -= 1
        if self.t[key] == 0:
            self.t.pop(key)
            if len(self.rev)>0:
                keys = self.rev.keys()
                self.max = max(keys)
                self.min = min(keys)
        else:
            self.insert(key)
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.max == None:
            return ""
        else:
            return list(self.rev[self.max])[0]
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.min == None:
            return ""
        else:
            return list(self.rev[self.min])[0]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()