class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        need = Counter(t)
        required = len(need)
        have = {}
        formed = 0
        left = 0
        best_len, best_left = float('inf'), 0

        for right, ch in enumerate(s):
            have[ch] = have.get(ch,0) + 1
            if ch in need and have[ch] == need[ch]:
                formed+=1
            while formed==required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]: 
                    formed -= 1
                left+=1
        return "" if best_len==float('inf') else s[best_left : best_left + best_len]
        