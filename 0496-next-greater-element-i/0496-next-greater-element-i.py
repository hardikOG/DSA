class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        nextGreater = [-1] * 10001
        stack = []

        for i in range(len(nums2) - 1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                nextGreater[nums2[i]] = stack[-1]
            else:
                nextGreater[nums2[i]] = -1

            stack.append(nums2[i])

        result = []

        for num in nums1:
            result.append(nextGreater[num])

        return result