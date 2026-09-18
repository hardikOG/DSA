class Solution(object):
    def sumOfUnique(self, nums):
        freq = {}
        total = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

            if freq[num] == 1:
                total += num
            elif freq[num] == 2:
                total -= num

        return total