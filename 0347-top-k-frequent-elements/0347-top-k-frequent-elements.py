class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        res = []
        
        for num in nums:
            freq[num] = freq.get(num, 0)+1
        mostFreq = sorted(freq.items(), key = lambda item: item[1], reverse = True)
        res = [item[0] for item in mostFreq[:k]]
        return res