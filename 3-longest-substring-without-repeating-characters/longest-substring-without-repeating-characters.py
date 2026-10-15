class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        result = 0
        last_seen = {}
        start = 0
        for end, ch in enumerate(s):
            if ch in last_seen:
                start = max(start, last_seen[ch] + 1)
            last_seen[ch] = end
            
            current_max = end - start + 1
            result = max(current_max, result)
            
        return result