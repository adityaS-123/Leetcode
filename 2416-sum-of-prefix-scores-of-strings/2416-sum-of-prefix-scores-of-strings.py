class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words):
        root = TrieNode()

        # Insert all words into the Trie and track the prefix counts
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.count += 1

        # Compute the sum of scores for every prefix of each word
        result = []
        for word in words:
            node = root
            score = 0
            for char in word:
                node = node.children[char]
                score += node.count
            result.append(score)
        
        return result
