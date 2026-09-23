class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = 0
        res = ""
        while right<len(s):
            if s[right] != " ":
                right+=1
            elif s[right] == " ":
                res += s[left:right+1][::-1]
                right+=1
                left=right
        res+=" "
        res+= s[left: right+2][::-1]
        return res[1:] 