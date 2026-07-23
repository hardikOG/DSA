# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        best = [0]
        def depth(node):
            
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            best[0] = max(best[0], L+R)
            return 1+ max(L,R)
        depth(root)
        return best[0]