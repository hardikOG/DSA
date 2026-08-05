class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        nxt = {}
        for num in nums2:
            while stack and stack[-1]<num:
                nxt[stack.pop()] = num
            stack.append(num)
        while stack:
            nxt[stack.pop()] = -1
        result = []
        for num in nums1:
            result.append(nxt[num])
        return result
