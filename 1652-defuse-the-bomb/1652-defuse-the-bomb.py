class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        res = [0]*n
        if k==0:
            return res
        start = 1 if k>0 else n+k
        end = k if k>0 else n-1
        window_sum = 0
        for i in range(start, end+1):
            window_sum += code[i%n]
        for i in range(n):
            res[i] = window_sum
            window_sum -= code[start%n]  #leaving element
            window_sum += code[(end+1) % n]  #incoming element
            start+=1
            end+=1
        return res