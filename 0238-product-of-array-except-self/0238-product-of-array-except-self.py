class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n  # Initialize the answer array with 1s
    
    # Pass 1: Calculate Prefix Products (Left to Right)
    # running_left holds the product of all elements to the left of index i
        running_left = 1
        for i in range(n):
            answer[i] = running_left
            running_left *= nums[i]  # Update the prefix product for the next index
        
    # Pass 2: Multiply by Suffix Products (Right to Left)
    # running_right holds the product of all elements to the right of index i
        running_right = 1
        for i in range(n - 1, -1, -1):  # Loop backwards from the last index to 0
            answer[i] *= running_right  # Multiply the existing prefix by the suffix
            running_right *= nums[i] # Update the suffix product for the next index
        
        return answer