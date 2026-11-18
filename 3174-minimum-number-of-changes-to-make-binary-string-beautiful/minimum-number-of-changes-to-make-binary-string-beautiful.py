class Solution:
    def minChanges(self, s: str) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(1)

        The problem allows multiple even-length partitions.
        Any valid even-length substring can be divided into length-2 substrings.
        Therefore, we don't need to explore different partition combinations.
        We independently fix each adjacent pair, changing one character if the pair differs
        """
        n = len(s)
        result = 0
        for i in range(0,n,2):
            if s[i] != s[i+1]:
                result += 1
        return result