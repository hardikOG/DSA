class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)

        window = n-k

        if window == 0:
            return sum(cardPoints)

        total = sum(cardPoints)

        # First window
        curr = sum(cardPoints[:window])

        # Best answer so far
        mini = curr

        # Slide the window
        for i in range(window, n):

            # Remove the element leaving the window
            curr -= cardPoints[i-window]

            # Add the new element entering the window
            curr += cardPoints[i]

            # Update minimum window seen so far
            mini = min(mini, curr)

        return total - mini
                