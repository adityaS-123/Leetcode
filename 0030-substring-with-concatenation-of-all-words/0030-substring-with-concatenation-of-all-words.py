from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Edge case: if the string or the words list is empty
        if not s or not words:
            return []
        
        # Length of each word
        word_len = len(words[0])
        # Total length of concatenation of all words
        total_len = word_len * len(words)
        # Count the occurrences of each word in words
        word_count = Counter(words)
        # List to store the starting indices of concatenated substrings
        result = []
        
        # Slide a window of length total_len over the string
        for i in range(len(s) - total_len + 1):
            # Get the current window of total_len
            substring = s[i:i + total_len]
            # Split the window into chunks of word_len and count them
            seen = []
            for j in range(0, total_len, word_len):
                seen.append(substring[j:j + word_len])
            seen_count = Counter(seen)
            
            # If the count of words in the window matches the expected word count
            if seen_count == word_count:
                result.append(i)
        
        return result
