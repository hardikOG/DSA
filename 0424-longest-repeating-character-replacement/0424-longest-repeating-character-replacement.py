import sys
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        low = 0
        res = 0
        n = len(s)
        freq = {}

        for high in range(n):
            freq[s[high]]=freq.get(s[high],0)+1

            length = high - low + 1
            max_cnt = max(freq.values())
            diff = length - max_cnt
            while diff > k:
                freq[s[low]]-=1
                low+=1
                max_cnt= max(freq.values())
                length = high - low + 1
                diff = length - max_cnt
            length = high - low +1
            res= max(res, length)
        return res