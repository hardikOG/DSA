class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        gp = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in gp:
                gp[key] = []
            gp[key].append(word)
        return list(gp.values())