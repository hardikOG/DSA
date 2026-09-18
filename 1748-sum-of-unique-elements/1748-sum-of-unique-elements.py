class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0)+1
        total = 0
        for num in nums:
            if freq[num] == 1:
                total+=num
        return total 