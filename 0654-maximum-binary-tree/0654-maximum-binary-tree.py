# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        st = []
        for num in nums:
            node = TreeNode(num)
            while st and st[-1].val<num:
                node.left = st.pop()
            if st:
                st[-1].right = node
            st.append(node)
        return st[0]



        
            