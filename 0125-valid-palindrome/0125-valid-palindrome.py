class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()

        s = ''.join(c for c in s if c.isalnum())
        if s == "":
            return True
        for c in s:
            if c.isalnum():
                if s[::-1] == s:
                    return True
                else:
                    return False

        return False