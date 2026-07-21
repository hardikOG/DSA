# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        from collections import deque
        q = deque([root])
        ans = []
        
        while q:
            size= len(q)
            total = 0 #needs to reset for each level
            for _ in range(size):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                total += node.val
            ans.append(float(total)/size)   #float is necessary for python2
        return ans
                
