class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1] * len(ratings)
        right = len(ratings)
        for i in range(1, right):
            if ratings[i]>ratings[i-1]:
                candies[i] = candies[i-1]+1
        for i in range(right-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
        return sum(candies)  
                