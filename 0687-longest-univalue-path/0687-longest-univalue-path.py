# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.length = 0
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            right_len = r + 1 if node.right and node.right.val == node.val else 0
            left_len = l+ 1 if node.left and node.left.val == node.val else 0
            self.length = max(self.length, left_len + right_len)
            return max(right_len, left_len)
            
        dfs(root)
        return self.length
            