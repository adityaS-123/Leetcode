class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        # Mappings from pattern to words and words to pattern
        char_to_word = {}
        word_to_char = {}
        
        for ch, word in zip(pattern, words):
            # Check if there's a consistent mapping from char to word
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                char_to_word[ch] = word
            
            # Check if there's a consistent mapping from word to char
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False
            else:
                word_to_char[word] = ch
        
        return True
