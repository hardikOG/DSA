# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        out = []
        if not root: return []
        out+=self.postorderTraversal(root.left)
        
        out+=self.postorderTraversal(root.right)

        out.append(root.val) 
        return out
        