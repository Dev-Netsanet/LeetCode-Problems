class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = max(len(word1), len(word2))
        new_word = ""
        for i in range(n):
            if i < len(word1):
                new_word += word1[i]
            if i < len(word2):
                new_word += word2[i]
        return new_word
    
sol = Solution()

print(sol.mergeAlternately("abc", "pqrw"))