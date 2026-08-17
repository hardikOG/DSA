class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)

        vowel_count = 0
        for i in range(k):
            if s[i] in vowel_set:
                vowel_count += 1

        max_vowels = vowel_count

        for i in range(n - k):
            char_leaving = s[i]
            if char_leaving in vowel_set:
                vowel_count -= 1

            char_entering = s[i + k]
            if char_entering in vowel_set:
                vowel_count += 1

            max_vowels = max(max_vowels, vowel_count)

            if max_vowels == k:
                return k

        return max_vowels