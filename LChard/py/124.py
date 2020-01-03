class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.single = 0
        self.double = 0

class Solution(object):
    def __init__(self):
        self.res=0
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=root.val
        self.helper(root)
        return self.res
    
    def helper(self,root):
        if root==None:
            return 0
        else :
            leftVal = self.helper(root.left)
            rightVal = self.helper(root.right)
            #这里要考虑到负数的情况
            root.single=max(leftVal,rightVal,0)+root.val
            root.double=max(leftVal+rightVal,leftVal,rightVal,0)+root.val
            self.res=max(self.res,root.double)
            return root.single 
            
            
        
        