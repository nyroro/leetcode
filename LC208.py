class Node(object):
    def __init__(self, c, end):
        self.val = c
        self.end = end
        self.next = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('', False)
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        now = self.root
        for character in word:
            if character not in now.next:
                now.next[character] = Node(character, False)
            now = now.next[character]
        now.end = True    
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        now = self.root
        for character in word:
            if character not in now.next:
                return False
            now = now.next[character]
        return now.end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        now = self.root
        for character in prefix:
            if character not in now.next:
                return False
            now = now.next[character]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)