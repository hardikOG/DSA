# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        from collections import deque
        q = deque([root])
        ans = []
        if not root:   #edge case empty tree
            return []
        while q:
            size = len(q)
            mx = float("-inf")  #inside while loop, to reset
            for _ in range(size):
                node = q.popleft()
                mx = max(mx, node.val)    #inside for loop
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(mx)

        return ans