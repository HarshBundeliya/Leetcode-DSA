import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Time Complexity = O(nlog(max(piles)))
        Space Complexity = O(1)
        
        when a condition changes monotonically from false to true, 
        binary search can find the first true value.
        """

        left = 1
        right = max(piles)
        possible_k = 0
        while left <= right:
            mid = (left+right)//2
            temp_h = 0
            for pile in piles:
                temp_h += (pile + mid - 1) // mid # math.ceil(pile/mid)
            if temp_h <= h:
                possible_k = mid
                right = mid - 1
            else:
                left = mid + 1
        return possible_k