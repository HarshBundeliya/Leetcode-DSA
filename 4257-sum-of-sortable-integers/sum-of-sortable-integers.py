
from math import isqrt

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n(n^(1/2)))
        Space Complexity: O(1)
        """
        n = len(nums)

        def is_sortable(k: int) -> bool:
            prev_max = None

            for start in range(0, n, k):
                end = start + k
                block_min = block_max = nums[start]
                descents = 0

                for i in range(start, end):
                    x = nums[i]
                    block_min = min(block_min, x)
                    block_max = max(block_max, x)

                    nxt = nums[start] if i == end - 1 else nums[i + 1]
                    if x > nxt:
                        descents += 1
                        if descents > 1:
                            return False

                # Sorted blocks must also be in global order.
                if prev_max is not None and prev_max > block_min:
                    return False

                prev_max = block_max

            return True

        ans = 0

        for d in range(1, isqrt(n) + 1):
            if n % d == 0:
                if is_sortable(d):
                    ans += d

                other = n // d
                if other != d and is_sortable(other):
                    ans += other

        return ans
