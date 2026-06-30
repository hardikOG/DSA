class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        pse = [-1] * n
        nse = [n] * n
        stack = []

        # Next Smaller Element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        stack = []

        # Previous Smaller Element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)

        total = 0

        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            total = (total + arr[i] * left * right) % MOD

        return total