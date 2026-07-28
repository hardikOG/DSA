class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jump_count = 0
        curr_jump_end = 0
        farthest_reach = 0
        for i in range(len(nums)-1):
            farthest_reach = max(farthest_reach, i+nums[i])
            if i == curr_jump_end:
                jump_count+=1
                curr_jump_end = farthest_reach
        return jump_count