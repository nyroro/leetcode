# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "*"
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        data = root.val
        return "(%s%s%s)"%(l, r, data)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(index):
            if data[index] == '*':
                return None, index+1
            if data[index] == '(':
                l, index = dfs(index+1)
                r, index = dfs(index)
                val, index = dfs(index)
                node = TreeNode(val)
                node.left = l
                node.right = r
                return node, index+1
            else:
                end = index
                while data[end]!=')':
                    end+=1
                ret =eval(data[index:end])
                return ret,end
            
                
            
        root, index = dfs(0)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))