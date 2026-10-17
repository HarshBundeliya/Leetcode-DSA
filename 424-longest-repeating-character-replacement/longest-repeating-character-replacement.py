class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        n = len(s)

        freq = {}
        for i in range(65,91):
            freq[i] = 0
        
        l = 0 
        best = 0
        for r in range(n):
            freq[ord(s[r])] += 1 
            while (r - l + 1) - max(freq.values()) > k:
                freq[ord(s[l])] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best