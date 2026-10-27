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
        while left < right:
            mid = (left+right)//2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid # math.ceil(pile/mid)
            if hours <= h:
                right = mid 
            else:
                left = mid + 1
        return left