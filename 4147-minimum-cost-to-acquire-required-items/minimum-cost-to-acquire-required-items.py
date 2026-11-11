class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        """
        Time Complexity = O(1)
        Space Complexity = O(1)
        """
        C1 = cost1*need1 + cost2*need2
        C2 = costBoth*max(need1,need2)
        if need1 < need2:
            C3 = need1*costBoth + (need2-need1)*cost2
        else:
            C3 = need2*costBoth + (need1-need2)*cost1
        
        if cost1 + cost2 < costBoth:
            return C1
        else:
            return min(C1,C2,C3)