from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        queue=deque()
        lastVisit=root
        while root or queue:
            while root:
                queue.append(root)
                root=root.left
            #先一直往左找，因为先返回的是左
            root =queue[-1]
            if root.right is None or root.right == lastVisit:
                res.append(root.val)
                queue.pop()
                lastVisit=root
                root=None
                #对当前节点判断一下，是该往上走了还是该往右走了，如果
            else:
                root=root.right
        return res
            
        