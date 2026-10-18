from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        """
        Time Complexity = O(n^2)
        Space Complexity = O(n^2)
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations C(n, r)
        comb = [[0] * n for _ in range(n)]

        for i in range(n):
            comb[i][0] = 1
            for j in range(1, i + 1):
                if j == i:
                    comb[i][j] = 1
                else:
                    comb[i][j] = (
                        comb[i - 1][j - 1] + comb[i - 1][j]
                    ) % MOD

        def count_ways(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = count_ways(left)
            right_ways = count_ways(right)

            # Interleave left and right subtree elements
            # while preserving their relative orders.
            interleavings = comb[len(left) + len(right)][len(left)]

            return (
                interleavings * left_ways % MOD * right_ways
            ) % MOD

        # Exclude the original ordering.
        return (count_ways(nums) - 1) % MOD