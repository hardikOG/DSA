from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = deque([])
        res = []
        queue.append(root)

        while len(queue) != 0:
            level = []
            size = len(queue)

            for _ in range(size):
                e = queue.popleft()
                level.append(e.val)

                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)

            res.append(level)

        return res