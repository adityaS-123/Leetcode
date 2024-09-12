from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If the lengths are not the same, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Use Counter to count frequencies of characters in both strings
        return Counter(s) == Counter(t)
