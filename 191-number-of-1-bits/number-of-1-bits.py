class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Time Complexity = O(31) = O(1)
        Space Complexity = O(1)
        """
        # count = 0
        # for i in range(30,-1,-1):
        #     if n - 2**i >= 0:
        #         n -= 2**i
        #         count += 1
        # return count

        """
        Time Complexity = O(k); where k is number of set bits
        Space Complexity = O(1)
        """
        count = 0 
        while n:
            n &= n-1
            count += 1
        return count
        """
        11 -> 1011

        11    1011
        &  ->      -> 1010 -> 10
        10    1010

        10    1010
        &  ->      -> 1000 -> 8
        9     1001

        8     1000
        &  ->      -> 0000 -> 0
        7     0111
        """