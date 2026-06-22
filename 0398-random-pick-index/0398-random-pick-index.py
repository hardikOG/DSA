class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        arr = self.indices[target]
        return arr[random.randint(0, len(arr)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)