class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Time complexity = O(n)
        # Space Complexity = O(1)
        res = 0
        current_max = 0
        l = 0
        r = len(height) - 1
        while l<r:
            current_max = min(height[l], height[r]) * (r-l)
            res = max(current_max, res)
            
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res