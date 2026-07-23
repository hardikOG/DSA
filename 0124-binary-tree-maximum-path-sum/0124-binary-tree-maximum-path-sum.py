# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxi = [float('-inf')]
        def dfs(node):
            if not node:
                return 0
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            maxi[0] = max(maxi[0], l + r + node.val)
            return node.val + max(l,r)
        dfs(root)
        return maxi[0]