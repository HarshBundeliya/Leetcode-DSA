class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxProfit(self, prices: list[int]) -> int:
        l,r = 0,1
        res = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l=r
            else:
                res = max(res,prices[r]-prices[l])
            r+=1
        return res

        