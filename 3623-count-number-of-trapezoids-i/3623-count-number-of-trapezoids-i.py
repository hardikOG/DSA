from collections import defaultdict

class Solution(object):
    def countTrapezoids(self, points):
        MOD = 10**9 + 7

        y_counts = defaultdict(int)

        for x, y in points:
            y_counts[y] += 1

        ans = 0
        prev = 0

        for count in y_counts.values():
            edges = count * (count - 1) // 2
            ans = (ans + edges * prev) % MOD
            prev = (prev + edges) % MOD

        return ans