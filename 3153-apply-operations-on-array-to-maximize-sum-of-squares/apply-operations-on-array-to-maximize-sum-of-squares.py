
from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # Time Complexity = O(n * B + k * B)
        # Space Complexity = O(B)
        # B = 30 (maximum number of bits)

        MOD = 10**9 + 7
        B = 30
        count = [0] * B

        for num in nums:
            for bit in range(B):
                if num & (1 << bit):
                    count[bit] += 1

        result = 0
        for _ in range(k):
            num = 0
            for bit in range(B):
                if count[bit] > 0:
                    num |= (1 << bit)
                    count[bit] -= 1

            result = (result + num * num) % MOD

        return result