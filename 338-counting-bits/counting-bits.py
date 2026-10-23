class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        result = []
        for i in range(n+1):
            count = 0
            while i:
                i = i & (i-1)
                count+=1
            result.append(count)
        return result