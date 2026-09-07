class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digit = set()
        for ch in s:
            if ch.isdigit():
                digit.add(int(ch))
        if len(digit)<2:
            return -1
        largest = float('-inf')
        second = float('-inf')
        for x in digit:
            if x>largest:
                second = largest
                largest = x
            elif largest>x>second:
                second = x
        return second