class Node(object):
    def __init__(self):
        self.end = False
        self.next = {}

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        now_node = self.root
        for character in word:
            if character not in now_node.next:
                now_node.next[character] = Node()
            now_node = now_node.next[character]
        now_node.end = True
                
    def dfs(self, now_node, index, word):
        if index == len(word):
            return now_node.end
        if word[index] == '.':
            for value in now_node.next.itervalues():
                if self.dfs(value, index+1, word):
                    return True
            return False
        if word[index] in now_node.next:
            return self.dfs(now_node.next[word[index]], index+1, word)
        return False
                

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, 0, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)