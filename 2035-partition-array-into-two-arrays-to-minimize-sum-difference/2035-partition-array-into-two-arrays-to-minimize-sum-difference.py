class Solution:
    def minimumDifference(self, nums):
        n=len(nums)//2
        A=[sorted(sum(x) for x in combinations(nums[:n],k)) for k in range(n+1)]
        B=[sorted(sum(x) for x in combinations(nums[n:],k)) for k in range(n+1)]
        S=sum(nums)
        T=S/2
        best=float('inf')
        for k in range(n+1):
            a = A[k]
            b = B[n-k]
            for ai in a:
                j = bisect_left(b, T-ai)
                if j<len(b):
                    best = min(best, abs(S-2*(ai+b[j])))
                if j:
                    best = min(best, abs(S-2*(ai+b[j-1])))
        return best