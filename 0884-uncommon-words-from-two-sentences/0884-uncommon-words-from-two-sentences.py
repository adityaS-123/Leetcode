from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Split the sentences into words and combine them
        words = s1.split() + s2.split()
        
        # Count the frequency of each word
        word_count = Counter(words)
        
        # Collect words that appear exactly once
        return [word for word in word_count if word_count[word] == 1]
