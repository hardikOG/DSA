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
        self.dia = 0

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)

            self.dia = max(self.dia,left+right)

            return 1 + max(left,right)

        height(root)
        return self.dia