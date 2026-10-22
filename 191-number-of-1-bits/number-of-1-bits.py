class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time Complexity = O(31) = O(1)
        # Space Complexity = O(1)
        count = 0
        for i in range(30,-1,-1):
            if n - 2**i >= 0:
                n -= 2**i
                count += 1
        return count