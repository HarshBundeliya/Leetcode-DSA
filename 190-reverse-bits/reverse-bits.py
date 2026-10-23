class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Time Complexity = O(32) = O(1)
        Space Complexity = O(1)
        """
        # result = 0
        # for i in range(31,-1,-1):
        #     if n & 1:
        #         result += 2**i
        #     n = n >> 1
        # return result

        result = 0
        for i in range(31,-1,-1):
            result = result<<1 | n&1
            n >>= 1
        return result