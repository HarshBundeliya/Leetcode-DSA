class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        result = 0
        seen = set()
        start = 0
        for end, ch in enumerate(s):
            if ch not in seen:
                seen.add(ch)
            else:
                while ch in seen:
                    seen.remove(s[start])
                    start += 1
                seen.add(ch)
            current_max = len(seen)
            result = max(current_max, result)
        return result