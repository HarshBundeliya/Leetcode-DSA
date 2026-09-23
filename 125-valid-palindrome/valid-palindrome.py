import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        new_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        l = 0
        r = len(new_s) - 1
        while l<r:
            if new_s[l] != new_s[r]:
                return False
            l+=1
            r-=1
        return True