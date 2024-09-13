class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        
        for word in strs:
            # Sort the word to create a key
            sorted_word = tuple(sorted(word))
            
            # If the sorted word is not in the dictionary, add it with the word in a list
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                # If the key already exists, append the word to the corresponding list
                anagrams[sorted_word].append(word)
        
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())
