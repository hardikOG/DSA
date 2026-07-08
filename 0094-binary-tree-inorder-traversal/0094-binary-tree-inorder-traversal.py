# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        curr = root
        stack = []
        inorder = []
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if not stack:
                    break
                curr = stack.pop()
                inorder.append(curr.val)
                curr = curr.right
        return inorder
