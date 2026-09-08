class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            ch = s[right]
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right

            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
        return max_len
