 def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if( root == None):
            return 0
        
        leftDepth = maxDepth(root.left)
        rightDepth = maxDepth(root.right)
        
        bigger = Math.max(leftDepth, rightDepth)
        
        return bigger + 1