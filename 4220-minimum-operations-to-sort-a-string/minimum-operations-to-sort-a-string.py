class Solution:
    def minOperations(self, s: str) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(1)
        """
        n = len(s)

        if all(s[i]<=s[i+1] for i in range(n-1)):
            return 0

        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        first = s[0]
        last = s[-1]

        if first==mn or last==mx:
            return 1
        for i in range(1,n-1):
            if s[i] == mx or s[i] == mn:
                return 2
        return 3