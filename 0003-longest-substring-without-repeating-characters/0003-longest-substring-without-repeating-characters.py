class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        l=0
        best = 0
        for r,c in enumerate(s):
            count[c] = count.get(c, 0)+1
            while count[c]>1:  #window invalid condition (when count>1)
                count[s[l]] -=1   
                l+=1
            best = max(best, r-l+1)
        return best
